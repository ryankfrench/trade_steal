'''
websocket session list
'''
from asgiref.sync import sync_to_async
from datetime import datetime
from asgiref.sync import sync_to_async

import json
import logging
import pytz

from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from main.consumers import SocketConsumerMixin

from main.models import Session
from main.models import parameter_set
from main.models.parameter_set import ParameterSet
# from main.globals import create_new_session_parameterset

class StaffHomeConsumer(SocketConsumerMixin):
    '''
    websocket session list
    '''    
    
    async def delete_session(self, event):
        '''
        delete specified session
        '''
        logger = logging.getLogger(__name__) 
        logger.info(f"Delete Session {event}")

        self.user = self.scope["user"]
        logger.info(f"User {self.user}")

        message_text = event["message_text"]

        status = await delete_session(message_text["id"], self.user)

        logger.info(f"Delete Session success: {status}")

        #build response
        message_data = {}
        message_data["sessions"] = await sync_to_async(get_session_list_json)(self.user)

        message = {}
        message["messageType"] = "get_sessions"
        message["messageData"] = message_data

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message,}, cls=DjangoJSONEncoder))

    async def create_session(self, event):
        '''
        create a new session
        '''
        logger = logging.getLogger(__name__) 
        logger.info(f"Create Session {event}")

        self.user = self.scope["user"]
        logger.info(f"User {self.user}")

        await sync_to_async(create_new_session)(self.user)
        
        #build response
        message_data = {}
        message_data["sessions"] = await sync_to_async(get_session_list_json)(self.user)

        message = {}
        message["messageType"] = event["type"]
        message["messageData"] = message_data

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message,}, cls=DjangoJSONEncoder))
    
    async def get_sessions(self, event):
        '''
        return a list of sessions
        '''
        logger = logging.getLogger(__name__) 
        logger.info(f"Get Sessions {event}")   

        self.user = self.scope["user"]
        logger.info(f"User {self.user}")     

        #build response
        message_data = {}
        message_data["sessions"] = await sync_to_async(get_session_list_json)(self.user)

        message = {}
        message["messageType"] = event["type"]
        message["messageData"] = message_data

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message,}, cls=DjangoJSONEncoder))
    
    async def get_sessions_admin(self, event):
        '''
        return a list of all sessions
        '''
        logger = logging.getLogger(__name__) 
        logger.info(f"Get Sessions Admin {event}")   

        self.user = self.scope["user"]
        logger.info(f"User {self.user}")     

        #build response
        message_data = {}
        message_data["sessions_admin"] = await sync_to_async(get_session_list_admin_json)(self.user)

        message = {}
        message["messageType"] = event["type"]
        message["messageData"] = message_data

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message,}, cls=DjangoJSONEncoder))


def create_new_session(auth_user):
    '''
    create an emtpy session and return it
    '''
    
    session = Session()

    parameter_set = ParameterSet()
    parameter_set.save()
    parameter_set.setup()

    session.parameter_set = parameter_set
    session.start_date = datetime.now(pytz.UTC)
    session.creator = auth_user
    session.current_period = 1

    session.save()
    session.update_player_count()

    logger = logging.getLogger(__name__) 
    logger.info(f"Create New Session {session}")

    return session

def get_session_list_json(usr):
    '''
    get list of sessions created by usr
    usr: auth user
    '''

    return list(Session.objects.filter(soft_delete=False, creator=usr)
                               .values('title', 'id', 'locked', 'start_date'))

def get_session_list_admin_json(usr):
    '''
    get list of all sessions if admin
    '''
    if usr.is_superuser:
        return list(Session.objects.filter(soft_delete=False) \
                              .order_by('-start_date') \
                              .values('title', 'id', 'locked', 'creator__last_name', 'creator__first_name', 'start_date'))
    else:
        return []

@sync_to_async
def delete_session(id_, user):
    '''
    delete specified session
    param: id_ {int} session id
    '''

    logger = logging.getLogger(__name__)   

    try:
        session = Session.objects.get(id=id_)

        #check ownership
        if session.creator != user and not user.is_superuser:
            logger.warning("delete_session: invalid user")
            return

        if settings.DEBUG:
            session.delete()
        else:
            session.soft_delete=True
            session.save()

        logger.info(f"Delete Session {id_}")
        return True
    except ObjectDoesNotExist:
        logger.warning(f"Delete Session, not found: {id}")
        return False

@sync_to_async
def get_session(id_):
    '''
    return session with specified id
    param: id_ {int} session id
    '''
    session = None
    logger = logging.getLogger(__name__)

    try:        
        session = Session.objects.get(id=id_)
        return session.json()
    except ObjectDoesNotExist:
        logger.warning(f"get_session session, not found: {id_}")
        return {}
    
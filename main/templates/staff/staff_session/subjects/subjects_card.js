 /**
 * take update player groups
 * @param messageData {json} session day in json format
 */
  takeUpdateConnectionStatus(messageData){
            
    if(messageData.status.value == "success")
    {
        let result = messageData.status.result;
        let session_players = app.$data.session.session_players;

        session_player = app.findSessionPlayer(result.id);

        if(session_player)
        {
            session_player.connected_count = result.connected_count;
        }
    }
},

/**
 * take update player groups
 * @param messageData {json} session day in json format
 */
 takeUpdateGroups(messageData){
    
    if(messageData.status.status == "success")
    {
        let group_list = messageData.status.group_list;
        let session_players = app.$data.session.session_players;

        for(let i=0; i<group_list.length; i++)
        {
            session_player = app.findSessionPlayer(group_list[i].id);

            if(session_player)
            {
                session_player.group_number = group_list[i].group_number;
            }
        }
    }
},

/** take name and student id
* @param messageData {json} session day in json format
*/
takeUpdateName(messageData){
           
    if(messageData.status.value == "success")
    {
        let result = messageData.status.result;

        session_player = app.findSessionPlayer(result.id);

        if(session_player)
        {
            session_player.name = result.name;
            session_player.student_id = result.student_id;
        }       
    }
 },

/** take name and student id
* @param messageData {json} session day in json format
*/
takeUpdateAvatar(messageData){
           
    if(messageData.status.value == "success")
    {
        let result = messageData.status.result;

        session_player = app.findSessionPlayer(result.id);

        if(session_player)
        {
            session_player.avatar = result.avatar;
            this.setupSingleAvatar(this.findSessionPlayerIndex(result.id));
        }       
    }
 },

/** take name and student id
* @param messageData {json} session day in json format
*/
takeNextInstruction(messageData){
           
    if(messageData.status.value == "success")
    {
        let result = messageData.status.result;

        session_player = this.findSessionPlayer(result.id);

        if(session_player)
        {
            session_player.current_instruction = result.current_instruction;
            session_player.current_instruction_complete = result.current_instruction_complete;
        }       
    }
 },

 /** take name and student id
* @param messageData {json} session day in json format
*/
takeFinishedInstructions(messageData){
           
    if(messageData.status.value == "success")
    {
        let result = messageData.status.result;

        session_player = this.findSessionPlayer(result.id);

        if(session_player)
        {
            session_player.instructions_finished = result.instructions_finished;
            session_player.current_instruction_complete = result.current_instruction_complete;
        }       
    }
 },

 /**
  * update subject earnings
  *  @param messageData {json} session day in json format
  */
 takeUpdateEarnings(messageData){

    if(messageData.status.value == "success")
    {
        let session_player_earnings = messageData.status.result.session_player_earnings;
        let session_players = this.session.session_players;

        for(let i=0; i<session_player_earnings.length; i++)
        {
            session_player = app.findSessionPlayer(session_player_earnings[i].id);

            if(session_player)
            {
                session_player.earnings = session_player_earnings[i].earnings;
            }
        }
    }
 },

 /**
  * return session player that has specified id
  */
 findSessionPlayer(id){

    let session_players = this.session.session_players;
    for(let i=0; i<session_players.length; i++)
    {
        if(session_players[i].id == id)
        {
            return session_players[i];
        }
    }

    return null;
 },

/**
 * return session player index that has specified id
 */
findSessionPlayerIndex(id){

    let session_players = app.$data.session.session_players;
    for(let i=0; i<session_players.length; i++)
    {
        if(session_players[i].id == id)
        {
            return i;
        }
    }

    return null;
},

/**
 * take update subjects production
 */
takeUpdateProductionTime(messageData){

    if(messageData.status.value == "success")
    {
       
        session_player = app.findSessionPlayer(messageData.status.result.id);
        
        session_player.good_one_production_rate = messageData.status.result.good_one_production_rate; 
        session_player.good_two_production_rate = messageData.status.result.good_two_production_rate;    
    }
},

/** send session update form   
*/
sendEmailList(){
    this.cancelModal = false;
    this.working = true;

    app.sendMessage("email_list",
                   {"csv_data" : this.csv_email_list});
},

/** take update subject response
 * @param messageData {json} result of update, either sucess or fail with errors
*/
takeUpdateEmailList(messageData){
    app.clearMainFormErrors();

    if(messageData.status.value == "success")
    {            
        $('#uploadEmailModal').modal('hide');    

        result = messageData.status.result;

        for(i=0; i<result.length; i++)
        {
            let session_player = app.findSessionPlayer(result[i].id);
            session_player.email = (result[i].email);
        }
    } 
    else
    {
        app.$data.cancelModal=true;                           
        app.displayErrors(messageData.status.errors);
    } 
},

/** show edit subject modal
*/
showSendEmailList(){
    app.clearMainFormErrors();
    this.cancelModal=true;

    this.csv_email_list = "";
    
    var myModal = new bootstrap.Modal(document.getElementById('uploadEmailModal'), {
        keyboard: false
        })

    myModal.toggle();
},

/** hide edit subject modal
*/
hideSendEmailList(){
    this.csv_email_list = "";

    if(this.cancelModal)
    {      
       
    }
},
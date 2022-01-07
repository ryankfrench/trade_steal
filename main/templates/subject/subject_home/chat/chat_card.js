sendChat(){

    if(this.working) return;
    if(this.chat_text.trim() == "") return;
    if(this.chat_text.trim().length > 200) return;
    
    this.working = true;
    app.sendMessage("chat", {"recipients" : this.chat_recipients,
                             "text" : this.chat_text.trim(),
                            });

    this.chat_text="";                   
},

/** take result of moving goods
*/
takeChat(messageData){
    //app.$data.cancelModal=false;
    //app.clearMainFormErrors();

    if(messageData.status.value == "success")
    {
        app.takeUpdateChat(messageData);                        
    } 
    else
    {
        
    }
},

/** take updated data from goods being moved by another player
*    @param messageData {json} session day in json format
*/
takeUpdateChat(messageData){
    
    let result = messageData.status;
    let chat = result.chat;
    let session_player = app.$data.session_player;

    if(result.chat_type=="All")
    {
        if(session_player.chat_all.length >= 100)
            session_player.chat_all.shift();

        session_player.chat_all.push(chat);
        if(app.$data.chat_recipients != "all")
        {
            session_player.new_chat_message = true;
        }
    }
    else
    {
        var sesson_player_target =  result.sesson_player_target;
        var session_players = app.$data.session.session_players;

        var target = -1;
        if(sesson_player_target == session_player.id)
        {
            target = result.chat.sender_id;
        }
        else
        {
            target = sesson_player_target;
        }

        for(let i=0; i<session_players.length; i++)
        {
            if(session_players[i].id == target)
            {
                
                if(session_players[i].chat_individual.length >= 100)
                    session_players[i].chat_individual.shift();

                session_players[i].chat_individual.push(chat);

                if(i != app.$data.chat_recipients_index)
                {
                    session_players[i].new_chat_message = true;
                }
                break;
            }
        }        
    }

    app.updateChatDisplay();
},

/** update who should receive chat
*    @param messageData {json} session day in json format
*/
updateChatRecipients(chat_recipients, chat_button_label, chat_recipients_index){
    app.$data.chat_recipients = chat_recipients;
    app.$data.chat_button_label = chat_button_label;
    app.$data.chat_recipients_index = chat_recipients_index;

    app.updateChatDisplay();

    if(app.$data.chat_recipients=="all")
    {
        app.$data.session_player.new_chat_message = false;
    }
    else
    {
        app.$data.session.session_players[chat_recipients_index].new_chat_message = false;
    }
},

/** update chat displayed on the screen
 */
updateChatDisplay(){

    if(app.$data.chat_recipients=="all")
    {
        app.$data.chat_list_to_display=Array.from(app.$data.session_player.chat_all);
    }
    else
    {
        app.$data.chat_list_to_display=Array.from(app.$data.session.session_players[app.$data.chat_recipients_index].chat_individual);
    }

    //add spacers
    for(let i=app.$data.chat_list_to_display.length;i<12;i++)
    {
        app.$data.chat_list_to_display.unshift({id:i*-1, text:"|", sender_id:app.$data.session_player.id})
    }

    //scroll to view
    if(app.$data.chat_list_to_display.length>0)
    {
        Vue.nextTick(() => {app.updateChatDisplayScroll()});        
    }
},

updateChatDisplayScroll(){
    var elmnt = document.getElementById("chat_id_" + app.$data.chat_list_to_display[app.$data.chat_list_to_display.length-1].id.toString());
    elmnt.scrollIntoView(); 
},


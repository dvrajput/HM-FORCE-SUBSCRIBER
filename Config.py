import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN",)
    DATABASE_URL = os.environ.get("DATABASE_URL",)
    APP_ID = os.environ.get("APP_ID",)
    API_HASH = os.environ.get("API_HASH",)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(1722652154)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1963338739:AAGiLliRy-1FCYbo8FxR2Js4VeSDV3xykO0"
    DATABASE_URL = "mongodb+srv://fsub:fsub@fsub.02g0n.mongodb.net/?retryWrites=true&w=majority"
    APP_ID = "8569540"
    API_HASH = "7643fb62451cd21337678f1f241f7b79"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1722652154)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**DV FORCE SUBSCRIBER**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @dvmoviesbackup**"
      ]

      START_MSG = "**I am DV FORCE SUBSCRIBER \n__Hey [{}](tg://user?id={})**\n__I can force members to join a your channel before writing messages in the group.\nLearn more at /help__ "

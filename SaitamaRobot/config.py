# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 4783634  # integer value, dont use ""
    API_HASH = "f6c33f46599246676f75e153b615dbbc"
    TOKEN = "1939252228:AAHO2XfD8z8GP6MBkohuBPsMB8Rfoqye-Ok"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1973983574  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Devilxfangx"
    SUPPORT_CHAT = 'OnePunchSupports'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1522747866  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1522747866  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI = 'mongodb+srv://friday:friday@cluster0.jhe6o.mongodb.net/cluster0?retryWrites=true&w=majority'
    REDIS_URL = 'redis://Botx:Garenaff@1@redis-17119.c54.ap-northeast-1-2.ec2.cloud.redislabs.com:17119/Botx'

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://deoxvvrd:kE3JdCk9Gb05C-1FSS7ZvNX89KiHNEd5@chunee.db.elephantsql.com/deoxvvrd'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '23323985'))
    API_HASH = str(getenv('API_HASH', 'd24809282e7c046a98a04ca3c66659e7'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','7966667864:AAHV3rVKSh8Oz_2nSBk8742wLhSu3gK2p1M'))
    name = str(getenv('name', 'file2linkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1003016985569'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '194.87.18.248'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6678306923").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'wipro_x'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('File2link'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '194.87.18.248:8080')) if not ON_HEROKU or getenv('FQDN', '194.87.18.248:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://falvo:FShMB8ufwkL0Gvt5@cluster0.9kut1hj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'GBEXTREM'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-10013626597")).split())) 
    
    

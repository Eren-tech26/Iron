class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "21968859"
    API_HASH = "21a59d21687f01d448530ee88a26b1eb"

    CASH_API_KEY = "0JMSACOEGPHOVRRI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002314716068)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://i.ibb.co/LzW4zt47/photo-2025-03-27-08-23-01-7486401934237106180.jpg"

    SUPPORT_CHAT = "https://t.me/igrischatsupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7522608342:AAEwrsx3n2VDNBRku93NPghwUeocACdt5Pw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "VQTNJC63SDEO"  # Get this value from https://timezonedb.com/api

    OWNER_ID =  "7774827065" # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

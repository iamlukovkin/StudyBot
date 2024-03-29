from . import settings
from .bot import my_bot as bot
from .bot import run
from .settings import BOT
from .settings import FOLDERS
from .settings import FILES

tutor_password: str = settings.BOT['tutor_password']
admins: list = settings.BOT['admin']

db_conn: str = "{dbms}+{module}://{db_user}:{db_pass}@{db_host}/{db_name}".format(
    
    dbms=settings.DATABASE[settings.APP['mode']]['DBMS'],
    module=settings.DATABASE[settings.APP['mode']]['MODULE'],
    db_user=settings.DATABASE[settings.APP['mode']]['USER'],
    db_pass=settings.DATABASE[settings.APP['mode']]['PASSWORD'],
    db_host=settings.DATABASE[settings.APP['mode']]['HOST'],
    db_name=settings.DATABASE[settings.APP['mode']]['NAME'],
    
)


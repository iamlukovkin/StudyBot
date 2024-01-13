import os
import dotenv
import datetime


dotenv_path: str = "config/.env"

APP: dict[str, str] = {

    'name': 'StudyBot',
    'version': '1.0.0',
    'mode': 'dev'
    
}

BOT: dict[str, str] = {
    
    'token': dotenv.get_key(dotenv_path, "BOT_TOKEN"),
    'tutor_password': dotenv.get_key(dotenv_path, "TUTOR_PASSWORD")

}

DATABASE: dict[str, str] = {
    
    'dev': {

        "DBMS": "mysql",
        "MODULE": "pymysql",
        "HOST": "localhost",
        "NAME": "StudyBotDB",
        "USER": dotenv.get_key(dotenv_path, "DB_USER_DEV"),
        "PASSWORD": dotenv.get_key(dotenv_path, "DB_PASSWORD"),
    },
    
    'prod': {
        
        "DBMS": "mysql",
        "MODULE": "pymysql",
        "HOST": "iamlukovkin.mysql.pythonanywhere-services.com",
        "NAME": "StudyBotDB",
        "USER": dotenv.get_key(dotenv_path, "DB_USER_PROD"),
        "PASSWORD": dotenv.get_key(dotenv_path, "DB_PASSWORD")
        
    }
        
}

static_folder: str = 'static/'
if not os.path.exists(static_folder): os.mkdir(static_folder)

FOLDERS: dict[str, str] = {
    
    'lessons': static_folder + 'lessons/',
    'exams': static_folder + 'exams/',
    'json': static_folder + 'jsons/',
    'temp': static_folder + 'temp/'
    
}

FILES: dict[str, str] = {
    'db_data': FOLDERS['json'] + 'data.json',
}

for folder in FOLDERS.values():
    if not os.path.exists(folder):
        os.mkdir(folder)


CONSTANTS: dict[str, str] = {
    'EVENT_DATE': datetime.datetime(2024, 2, 5)
}

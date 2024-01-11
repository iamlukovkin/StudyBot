import dotenv


dotenv_path: str = "config/.env"

APP: dict[str, str] = {

    'name': 'StudyBot',
    'version': '1.0.0',
    'mode': 'dev'
    
}

BOT: dict[str, str] = {
    
    'token': dotenv.get_key(dotenv_path, "BOT_TOKEN")
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

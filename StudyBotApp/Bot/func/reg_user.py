from telebot.types import Message
from config import bot
from database import *

from Bot import views

def _(message: Message):
    """
    Start command
    
    :param message:
    :return: bool 
    """
    
    user_id: int = message.from_user.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    if not user:
        
        fullname: str = message.from_user.first_name \
            if message.from_user.first_name else ""
        if message.from_user.last_name:
            fullname += " " + message.from_user.last_name
        user: User = User(
            
            user_id=user_id,
            username=message.from_user.username,
            fullname=fullname,
            studgroup="Не указана",
            
        )
        
        try:
            session.add(user)
            session.commit()
            message_text = 'Регистрация прошла успешно'
        
        except Exception as e:
            print(f"Error while adding new user: {e}")
            session.rollback()
            _(message)
        
        finally:
            session.close()
    
    else:
        message_text = 'Вы уже зарегистрированы'
        
    bot.send_message(chat_id=message.chat.id, text=message_text)

    views.main_menu(message)
    
    return 
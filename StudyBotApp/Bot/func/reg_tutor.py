from telebot.types import Message
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from config import bot
from config import tutor_password
from database import *
from .check_user_exists import _ as check_user_exists
from .reg_user import _ as reg_user

from Bot import views


def _(message: Message):
    """
    Регистрация преподавателя
    
    Args:
        message (Message): Сообщение
        
    Returns:
        None
    """
    
    user_id: int = message.chat.id
    user: User | bool = check_user_exists(message)
    keyboard: InlineKeyboardMarkup = views.homepage_keyboard
    
    if not user:
        
        bot.send_message(
            
            chat_id=user_id, 
            text='Вы не зарегистрированы в боте'
            
        )
        
        views.reg_user(message)
        
        return 
       
    if not user.is_tutor:
        
        message_text: str = 'Для регистрации в боте в роли ' \
        'преподавателя вам необходимо ввести пароль, ' \
        'который вы можете взять у администратора @iamlukovkin'
        
        bot.send_message(
            
            chat_id=user_id, 
            text=message_text,
            reply_markup=keyboard
            
        )
    
        bot.register_next_step_handler_by_chat_id(
            
            chat_id=user_id,
            callback=reg_tutor_password
            
        )
    
    else:
        
        message_text: str = 'Вы уже зарегистрированы в роли преподавателя'
        
        bot.send_message(
            chat_id=user_id, 
            text=message_text,
            reply_markup=keyboard
            
        )

    return
    
    
def reg_tutor_password(message: Message):
    
    user_id: int = message.chat.id
    
    if message.text == tutor_password:
        
        session = get_session()
        user: User | bool = check_user_exists(message)
        session.query(User).filter(
            User.user_id == user_id).update({User.is_tutor: True})
        session.commit()
        
        bot.send_message(
            
            chat_id=user_id, 
            text='Вы успешно зарегистрированы в роли преподавателя'
            
        )
        
        views.main_menu(message)
    
    else:
        
        bot.send_message(chat_id=user_id, text='Неверный пароль')
        
        views.main_menu(message)
        
    return
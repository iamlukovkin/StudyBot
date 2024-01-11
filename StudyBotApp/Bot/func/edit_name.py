from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from config import bot
from database import *

from Bot import views


def _(message):

    user_id: int = message.chat.id
    message_text: str = 'Пришлите свое имя (<i>рекомендуется писать ФИО полностью</i>)'
    session: session = get_session()
    
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=message_text
        
    )
    
    keyboard.add(KeyboardButton(
        
        text=user.fullname
        
    ))

    bot.send_message(
        
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=keyboard
        
    )
    
    bot.register_next_step_handler_by_chat_id(
        
        chat_id=message.chat.id,
        callback=update_name
    
    )
    

def update_name(message):
    
    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    if len(message.text) <= 100:
        user.fullname = message.text
        session.commit()
    
        bot.send_message(
            
            chat_id=message.chat.id,
            text='Имя изменено'
            
        )
        
        views.main_menu(message)
    
    else:
        bot.send_message(
            
            chat_id=message.chat.id,
            text='Некорректный ввод'
            
        )
        
        views.profile_menu(message)
    
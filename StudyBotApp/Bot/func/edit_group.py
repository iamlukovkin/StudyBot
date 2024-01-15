from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ReplyKeyboardRemove
from telebot.types import KeyboardButton
from config import bot
from database import *

from Bot import views


def _(message):

    user_id: int = message.chat.id
    message_text: str = 'Пришлите номер группы'
    session: session = get_session()
    
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        
        resize_keyboard=True,
        one_time_keyboard=True
        
    )
    
    keyboard.add(KeyboardButton(
        
        text=user.get_group()
        
    ))

    bot.send_message(
        
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=keyboard
        
    )
    
    bot.register_next_step_handler_by_chat_id(
        
        chat_id=message.chat.id,
        callback=update_group
    
    )
    

def update_group(message):
    
    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    new_group: str = 'gr_' + message.text
    if len(new_group) <= 20:
        user.studgroup = new_group
        session.commit()
    
        bot.send_message(
            
            chat_id=message.chat.id,
            text='Группа изменена',
            reply_markup=ReplyKeyboardRemove()
            
        )
        
        views.main_menu(message)
    
    else:
        bot.send_message(
            
            chat_id=message.chat.id,
            text='Некорректный ввод',
            reply_markup=ReplyKeyboardRemove()
            
        )
        
        views.profile_menu(message)
    
    
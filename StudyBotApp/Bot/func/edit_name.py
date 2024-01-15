from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ReplyKeyboardRemove
from telebot.types import KeyboardButton
from config import bot
from database import *

from Bot import views


def _(message):

    user_id: int = message.chat.id
    message_text: str = 'Пришлите свое имя (<i>рекомендуется писать ФИО полностью</i>)'
    session: session = get_session()
    try:
        user: User = session.query(
            User).filter(User.user_id == user_id).first()
    except:
        session.rollback()
    finally:
        session.close()
    
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        
        resize_keyboard=True,
        one_time_keyboard=True
        
    )
    
    keyboard.add(KeyboardButton(text=user.fullname))

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
        
        if user.is_tutor:
            rating_tutor: RaitingTutor = session.query(
                RaitingTutor).filter(RaitingTutor.tutor_name == user.fullname).first()
            if rating_tutor is None:
                rating_tutor: RaitingTutor = RaitingTutor(
                    tutor_name=message.text,
                    count=0
                )
                session.add(rating_tutor)
            else:
                rating_tutor.tutor_name = message.text
            session.commit()
        
        user.fullname = message.text
        session.commit()
        session.close()
    
        bot.send_message(
        
            chat_id=message.chat.id, 
            text='Имя изменено',
            reply_markup=ReplyKeyboardRemove()
        
        )
        
        views.main_menu(message)
    
    else:
        bot.send_message(chat_id=message.chat.id, text='Некорректный ввод')
        
        views.profile_menu(message)
    
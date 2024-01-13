import datetime
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from config import bot
from database import *

from Bot import views


def _(message):

    user_id: int = message.chat.id
    message_text: str = 'Пришлите свое сообщение, и я помогу вам'
    
    bot.send_message(
        
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=views.homepage_keyboard
        
    )
    
    bot.register_next_step_handler_by_chat_id(
        
        chat_id=message.chat.id,
        callback=send_support_message
    
    )
    

def send_support_message(message):
    
    user_id: int = message.chat.id
    session: session = get_session()
    
    support_message: Support = Support(
        user_id=user_id,
        message=message.text,
        date=datetime.datetime.now().strftime("%d.%m.%Y"),
        time=datetime.datetime.now().strftime("%H:%M")
    )
    try:
        session.add(support_message)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()
        
    bot.send_message(
        chat_id=message.chat.id,
        text='Сообщение отправлено, спасибо за обратную связь',
        reply_markup=views.homepage_keyboard
    )
    
    admins: User = session.query(
        User).filter(User.is_admin == True).all()
    
    for admin in admins:
        bot.send_message(
            chat_id=admin.user_id,
            text='<b>Новое сообщение от пользователя</b>\n' + message.text,
            reply_markup=views.homepage_keyboard
        )
    
    return
    
    
    
    
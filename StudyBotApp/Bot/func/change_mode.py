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
    user_id: int = message.chat.id
    user: User | bool = check_user_exists(message)
    
    if not user.is_admin:
        return
    
    mode = False if user.is_tutor else True
    session = get_session()
    session.query(User).filter(
        User.user_id == user_id).update(
            {User.is_tutor: mode}
    )
    
    session.commit()
    
    bot.send_message(
        chat_id=user_id,
        text='Режим изменен'
    )
    
    views.main_menu(message)
    
    return
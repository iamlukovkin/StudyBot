from telebot.types import Message
from telebot.types import InlineKeyboardMarkup

from database import *
from config import bot
from Bot.views.assets import *
import Bot

def _(message: Message):
    
    user_id: int = message.chat.id
    message_text: str = homepage_text
    session: session = get_session()
    
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    if user.is_admin:
        keyboard: InlineKeyboardMarkup = admin_keyboard
    elif user.is_tutor:
        keyboard: InlineKeyboardMarkup = home_tutor_keyboard
    else:
        keyboard: InlineKeyboardMarkup = home_student_keyboard
    
    bot.send_message(
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=keyboard
    )
    
    return
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup

from database import *
from config import bot
from Bot.views.assets import *
import Bot


def _(message: Message):
    
    user_id: int = message.chat.id
    
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    if '_' in user.studgroup:
        group: str = user.studgroup.split('_')[1]
    
    else:
        group: str = user.studgroup
        
    message_text: str = profile_info(user)
    
    if user.is_tutor:
        keyboard: InlineKeyboardMarkup = tutor_profile_keyboard
    else:
        keyboard: InlineKeyboardMarkup = student_profile_keyboard
    
    bot.send_message(
        
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=keyboard
    
    )
    
    return
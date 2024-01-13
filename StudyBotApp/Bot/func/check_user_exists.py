from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from config import bot
from database import *

from Bot import views


def _(message: Message):
    
    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    
    if user is not None:
        return user
        
    else:
        return False

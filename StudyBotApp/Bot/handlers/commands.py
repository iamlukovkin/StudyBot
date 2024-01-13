from config import bot
from telebot.types import Message
from Bot import func
from Bot.views import interface


@bot.message_handler(commands=['start'])
def start(message: Message):
    
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    
    func.reg_user(message)
    
    return


@bot.message_handler(commands=['profile'])
def profile(message: Message):
    
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    
    interface.profile_menu(message)
    
    return


@bot.message_handler(commands=['reg_tutor'])
def reg_tutor(message: Message):
    
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    
    func.reg_tutor(message)
    
    return

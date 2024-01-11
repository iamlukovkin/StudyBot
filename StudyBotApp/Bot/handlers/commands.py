from config import bot
from telebot.types import Message
from Bot import func
from Bot.views import interface


@bot.message_handler(commands=['start'])
def start(message: Message):
    
    func.check_user(message)
    
    return


@bot.message_handler(commands=['profile'])
def profile(message: Message):
    
    interface.profile_menu(message)
    

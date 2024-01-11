from telebot import TeleBot
from telebot import logger
import logging
from . import settings


my_bot: TeleBot = TeleBot(
    
    token=settings.BOT['token'],
    parse_mode='HTML',

)


def run() -> None:
    """
    Run bot.
    """
    
    telebot_logger: Logger = logger
    telebot_logger.setLevel(logging.INFO)
    
    my_bot.infinity_polling()

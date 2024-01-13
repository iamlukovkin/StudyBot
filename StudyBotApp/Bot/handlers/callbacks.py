from config import bot
from telebot.types import CallbackQuery
from Bot import func

from Bot.views import *


@bot.callback_query_handler(
    func=lambda call: call.data == profile_button.callback_data)
def my_profile(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    profile_menu(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == back_button.callback_data)
def back_home(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    main_menu(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == edit_group_button.callback_data)
def edit_group(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.edit_group(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == edit_name_button.callback_data)
def edit_name(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.edit_name(query.message)
    
    return
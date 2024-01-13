from config import bot
from telebot.types import CallbackQuery
from Bot import func
import Manager
from database import *

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

@bot.callback_query_handler(
    func=lambda call: call.data == update_database_button.callback_data)
def update_database(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    user_id: int = query.message.chat.id
    user: User = func.check_user_exists(query.message)
    if not user.is_admin:
        return
    
    func.update_database(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == lessons_button.callback_data)
def lessons(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    lessons_menu(query.message)    
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == student_lessons_today_button.callback_data)
def student_lessons_today(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.student_lessons_today(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == student_lessons_tomorrow_button.callback_data)
def student_lessons_tomorrow(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.student_lessons_tomorrow(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == tutor_lessons_today_button.callback_data)
def tutor_lessons_today(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.tutor_lessons_today(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == tutor_lessons_tomorrow_button.callback_data)
def tutor_lessons_tomorrow(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.tutor_lessons_tomorrow(query.message)
    
    return

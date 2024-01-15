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


@bot.callback_query_handler(
    func=lambda call: call.data == student_lessons_all_button.callback_data)
def student_lessons_all(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.student_lessons_all(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == tutor_lessons_all_button.callback_data)
def tutor_lessons_all(query: CallbackQuery):

    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.tutor_lessons_all(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == change_mode_button.callback_data)
def change_mode(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.change_mode(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == exams_button.callback_data)
def exams(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.exams(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == support_button.callback_data)
def support(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.support(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == tutors_info_button.callback_data)
def tutors_info_menu(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    tutors_info(query.message)
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == stud_tutor_today_button.callback_data)
def stud_tutor_today(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.search_tutor(query.message, 'today')
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == stud_tutor_tomorrow_button.callback_data)
def stud_tutor_tomorrow(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.search_tutor(query.message, 'tomorrow')
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data == stud_tutor_all_button.callback_data)
def stud_tutor_tomorrow(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    
    func.search_tutor(query.message, 'all')
    
    return


@bot.callback_query_handler(
    func=lambda call: call.data.startswith('search_tutor_'))
def search_tutor_by_id_query(query: CallbackQuery):
    
    bot.clear_step_handler_by_chat_id(chat_id=query.message.chat.id)
    call_data: list = query.data.split('_')
    search_mode: str = call_data[-2]
    tutor_id: int = int(call_data[-1])
    func.search_tutor_by_id(query.message, search_mode, tutor_id)
    
    return

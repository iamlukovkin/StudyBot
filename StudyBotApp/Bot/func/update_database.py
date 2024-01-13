from telebot.types import Message
from config import bot
from database import *

import Manager
from Bot import views


def _(message: Message):
    
    bot.send_message(chat_id=message.chat.id,
        text='Загрузка данных. Пожалуйста, подождите...')
    
    lessons_added, lessons_skipped, \
    exams_added, exams_skipped = Manager.update_database(
        require_download=False)
    
    message_text: str = 'Данные обновлены.\n'
    message_text += f'Добавлено {lessons_added} занятий: '
    message_text += f'и {exams_added} экзаменов.\n'
    message_text += f'Пропущено {lessons_skipped} занятий: '
    message_text += f'и {exams_skipped} экзаменов.\n'
    
    bot.send_message(chat_id=message.chat.id, text=message_text,
        reply_markup=views.admin_keyboard)

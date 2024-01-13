import os
from telebot.types import Message
from config import bot
from config import FOLDERS
from database import *
import Manager
from sqlalchemy import text

from Bot import views


def _(message: Message):

    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    session.close()
    
    if user.is_tutor:
        param = user.fullname
        search_by = 'tutor'
        filename_param = user.fullname
    
    else:
        param = user.studgroup
        search_by = 'group'
        filename_param = user.get_group()
    
    filename: str = "Расписание экзаменов: " + filename_param
    doc = Manager.create_exam(filename, param, search_by)
    path = FOLDERS['docs'] + filename + '.docx'
    doc.save(path)
    
    bot.send_document(chat_id=message.chat.id, document=open(path, 'rb'))
    os.remove(path)
    bot.send_message(
        chat_id=user_id, 
        text='Документ: {} отправлен.'.format(
            filename),
        reply_markup=views.homepage_keyboard
    )
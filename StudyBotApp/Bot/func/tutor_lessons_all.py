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
    
    lessons = session.query(
        Lesson).filter(Lesson.lesson_info.like('%{}%'.format(
            user.fullname))).all()
        
    if len(lessons) == 0:
        bot.send_message(
            chat_id=user_id, 
            text='По вашему запросу ничего не найдено.',
            reply_markup=views.homepage_keyboard
        )
        return
    
    filename: str = "Расписание преподавателя " + user.fullname
    doc = Manager.create_doc(filename, user.fullname, search_by='tutor')
    session.close()
    path = FOLDERS['docs'] + filename + '.docx'
    doc.save(path)
    
    bot.send_document(chat_id=message.chat.id, document=open(path, 'rb'))
    os.remove(path)
    bot.send_message(
        chat_id=user_id, 
        text='Документ "{}" отправлен.'.format(filename),
        reply_markup=views.homepage_keyboard
    )
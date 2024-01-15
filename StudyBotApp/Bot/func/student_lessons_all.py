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
    group: str = user.get_group()
    session.close()
    
    filename: str = "Расписание группы " + user.get_group()
    doc = Manager.create_doc(filename, user.studgroup)
    path = FOLDERS['docs'] + filename + '.docx'
    doc.save(path)
    
    bot.send_document(chat_id=message.chat.id, document=open(path, 'rb'))
    os.remove(path)
    message_text: str = 'Документ: {} отправлен.\n\n'.format(filename)
    message_text += views.lessons_info_text
    bot.send_message(
        chat_id=user_id, 
        text=message_text,
        reply_markup=views.lessons_info_keyboard
    )
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup
from config import bot
from database import *
import Manager

from Bot import views


def _(message: Message):

    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    group: str = user.get_group()
    session.close()
    
    week, day = Manager.today()
    session: session = get_session()
    today_lessons = session.query(Lesson).filter(
        Lesson.group == group).filter(
            Lesson.day == day).filter(
                Lesson.week == week).all()
    session.close()
    
    message_text = '<b>Сегодня:</b> {}, {}\n\n'.format(day, week)
    if len(today_lessons) == 0:
        message_text += 'На сегодня пар нет\n\n'
        
    else:
        for lesson in today_lessons:
            lesson: Lesson
            message_text += lesson.get_info()
            
    message_text += views.lessons_info_text
    
    keyboard: InlineKeyboardMarkup = views.lessons_info_keyboard
    
    bot.send_message(chat_id=message.chat.id, text=message_text,
        reply_markup=keyboard)
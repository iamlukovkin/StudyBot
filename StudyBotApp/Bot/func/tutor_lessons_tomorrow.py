from telebot.types import Message
from config import bot
from database import *
import Manager

from Bot import views


def _(message: Message):
    
    user_id: int = message.chat.id
    session: session = get_session()
    user: User = session.query(
        User).filter(User.user_id == user_id).first()
    tutor: str = user.fullname
    session.close()
    
    week, day = Manager.tomorrow()
    session: session = get_session()
    tomorrow_lessons = session.query(Lesson).filter(
        Lesson.lesson_info.like('%{}%'.format(tutor))).filter(
            Lesson.day == day).filter(
                Lesson.week == week).all()
    
    message_text = '<b>Завтра:</b> {}, {}\n\n'.format(day, week)
    if len(tomorrow_lessons) == 0:
        message_text += 'На завтра пар нет\n\n'
        
    else:
        for lesson in tomorrow_lessons:
            lesson: Lesson
            message_text += lesson.get_info()
            
    message_text += views.lessons_info_text
    
    keyboard: InlineKeyboardMarkup = views.lessons_info_keyboard
    
    bot.send_message(chat_id=message.chat.id, text=message_text,
        reply_markup=keyboard)
    

import os
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup
from config import bot
from config import FOLDERS
from database import *
import Manager

from Bot import views


def search_tutor(message, mode: str):
    
    user_id: int = message.chat.id
    
    message_text, keyboard = views.tutors_rating(mode)

    bot.send_message(
        
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=keyboard
        
    )
    
    bot.register_next_step_handler_by_chat_id(
        
        chat_id=message.chat.id,
        callback=search_tutor_message,
        mode=mode
    
    )


def search_tutor_message(message: Message, mode: str):
    
    user_id: int = message.chat.id
    session: session = get_session()
    request: str = message.text
    tutor: RaitingTutor = session.query(
        RaitingTutor).filter(RaitingTutor.tutor_name == request).first()
    
    if tutor is None:
        tutor = RaitingTutor(
            tutor_name=request,
            count=1
        )
        session.add(tutor)
    else:
        tutor.increase_count()
    session.commit()
    tutor_id = tutor.id
    session.close()
    
    search_tutor_by_id(message, mode, tutor_id)
    
    return


def search_tutor_by_id(message: Message, mode: str, tutor_id: int):
    
    session: session = get_session()
    tutor: RaitingTutor = session.query(
        RaitingTutor).filter(RaitingTutor.id == tutor_id).first()
    tutor.increase_count()
    session.commit()
    
    if mode == 'today':
        week, day = Manager.today()
        lessons = session.query(Lesson).filter(
            Lesson.lesson_info.like(
                '%{}%'.format(tutor.tutor_name))).filter(
                Lesson.day == day).filter(
                    Lesson.week == week).all()
                
    elif mode == 'tomorrow':
        week, day = Manager.tomorrow()
        lessons = session.query(Lesson).filter(
            Lesson.lesson_info.like(
                '%{}%'.format(tutor.tutor_name))).filter(
                Lesson.day == day).filter(
                    Lesson.week == week).all()
    else:
        lessons: list = session.query(Lesson).filter(
            Lesson.lesson_info.like(
                '%{}%'.format(tutor.tutor_name))).all()
        
    session.close()
    if mode == 'today': calendar_day = 'Сегодня'
    elif mode == 'tomorrow': calendar_day = 'Завтра'
    if mode == 'today' or mode == 'tomorrow':
        message_text = '<b>{}:</b> {}, {}\n\n'.format(
        calendar_day,day, week)
    if len(lessons) == 0:
        if mode == 'today':
            message_text += \
                'На сегодня у преподавателя <b>{}</b> пар нет\n\n'.format(
                    tutor.tutor_name)
        elif mode == 'tomorrow':
            message_text += \
                'На завтра у преподавателя <b>{}</b> пар нет\n\n'.format(
                    tutor.tutor_name)
        else:
            message_text: str = 'У этого преподавателя пар нет\n\n'
        
    else:
        if mode == 'today': calendar_day = 'Сегодня'
        elif mode == 'tomorrow': calendar_day = 'Завтра'
        if mode == 'today' or mode == 'tomorrow':
            
            day_dict: dict = {}
            for lesson in lessons:
                lesson: Lesson
                
                string_text: str = '{0}\n' 
                string_text += 'Начало: {1}' 
                string_text += '\nПерерыв: {2}'
                
                if lesson.time_end:
                    string_text += '\nКонец: {3}' 
                
                if lesson.time_start not in day_dict:
                    start_time, break_time, end_time = lesson.get_times()
                    day_dict[lesson.time_start] = [
                        [lesson.get_group()], 
                        string_text.format(
                            lesson.lesson_info,
                            start_time.strftime('%H:%M'),
                            break_time.strftime('%H:%M'),
                            end_time.strftime('%H:%M')
                        )
                    ]
                else:
                    day_dict[lesson.time_start][0].append(
                        lesson.get_group())
            for time in day_dict:
                if len(day_dict[time][0]) > 1:
                    prefix = 'Группы: '
                else:
                    prefix = 'Группа: '
                message_text += '<b>{}</b>\n{}\n\n'.format(
                    prefix + ', '.join(day_dict[time][0]), 
                    day_dict[time][1]                
                )
        else:
            filename: str = 'Расписание преподавателя ' + tutor.tutor_name
            doc = Manager.create_doc(
                filename, tutor.tutor_name, search_by='tutor')
            doc.save(FOLDERS['docs'] + filename + '.docx')
            message_text = 'Документ "{}" отправлен.\n\n'.format(filename)
            bot.send_document(chat_id=message.chat.id, document=open(
                FOLDERS['docs'] + filename + '.docx', 'rb'))
            os.remove(FOLDERS['docs'] + filename + '.docx')
            
    message_text += views.homepage_text_kb
    
    keyboard: InlineKeyboardMarkup = views.tutors_back_keyboard
    
    bot.send_message(chat_id=message.chat.id, text=message_text,
        reply_markup=keyboard)
    
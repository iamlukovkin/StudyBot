from database import *
from .inline_buttons import *
from telebot.types import InlineKeyboardMarkup

homepage_text: str = \
    '<b>Домашняя страница</b> \n\n' \
    '{0.text} - Профиль \n'\
    '{1.text} - Занятия \n'\
    '{2.text} - Экзамены \n'\
    '{3.text} - Расписание преподавателя\n'\
    '{4.text} - Связаться с нами'.format(
        
        profile_button, lessons_button, 
        exams_button, tutors_info_button, support_button
        
    )


profile_text: str = \
    '<b>Профиль</b> \n\n' \
    'Имя: {0} \n' \
    'Группа: {1} \n\n' \
    '{2.text} - Изменить имя \n' \
    '{3.text} - Изменить группу\n' \
    '{4.text} - Назад'
    

profile_text_tutor: str = \
    '<b>Профиль</b> \n\n' \
    'Имя: {0} \n' \
    'Роль: преподаватель \n\n' \
    '{1.text} - Изменить имя\n' \
    '{2.text} - Назад' 


def profile_info(user: User) -> str:
    
    if user.is_tutor:
        return profile_text_tutor.format(
            user.fullname, edit_name_button, back_button
        )
    
    else:
        return profile_text.format(user.fullname, user.get_group(), 
            edit_name_button, edit_group_button, back_button
        )


lessons_text_student: str = \
    '<b>Занятия</b> \n\n' \
    '{0.text} - Занятия на сегодня \n' \
    '{1.text} - Занятия на завтра \n' \
    '{2.text} - Полное расписание \n' \
    '{3.text} - Назад'.format(
        student_lessons_today_button,
        student_lessons_tomorrow_button,
        student_lessons_all_button,
        back_button
)
    
lessons_text_tutor: str = \
    '<b>Занятия</b> \n\n' \
    '{0.text} - Занятия на сегодня \n' \
    '{1.text} - Занятия на завтра \n' \
    '{2.text} - Полное расписание \n' \
    '{3.text} - Назад'.format(
        tutor_lessons_today_button,
        tutor_lessons_tomorrow_button,
        tutor_lessons_all_button,
        back_button
)


def lessons_text(user: User) -> str:
    
    if user.is_tutor:
        return lessons_text_tutor
    
    else:
        return lessons_text_student

lessons_info_text: str = \
    '{0.text} - Занятия\n' \
    '{1.text} - Назад\n'.format(
        lessons_button, back_button
)

homepage_text_kb: str = \
    '{0.text} - Домашняя страница \n'.format(
        homepage_button
    )
        


tutors_info: str = \
    '<b>Расписание преподавателя</b> \n\n' \
        '{0.text} - Расписание на сегодня\n' \
        '{1.text} - Расписание на завтра\n' \
        '{2.text} - Полное расписание\n' \
        '{3.text} - Назад'.format(
            stud_tutor_today_button,
            stud_tutor_tomorrow_button,
            stud_tutor_all_button,
            back_button
        )
        
        
def tutors_rating(mode: str) -> str:
    
    message_text: str = 'Введите ФИО преподавателя\n'\
        '<i>Рекомендуется писать ФИО полностью.</i>\n'\
        
    session: session = get_session()
    tutors = session.query(RaitingTutor).order_by(
        RaitingTutor.count.desc()).limit(5).all()
    session.close()
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()
    if len(tutors) != 0:
        message_text += 'наиболее популярные запросы представлены ниже\n\n'
    for tutor in tutors:
        tutor: RaitingTutor
        message_text += tutor.tutor_name + ' - ' + str(tutor.count) + '\n'
        keyboard.add(InlineKeyboardButton(
            text=tutor.tutor_name, 
            callback_data='search_tutor_'+mode+'_'+str(tutor.id)))
    keyboard.add(homepage_button)
        
    return message_text, keyboard
    
    
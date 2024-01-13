from database import *
from .inline_buttons import *

homepage_text: str = \
    '<b>Домашняя страница</b> \n\n' \
    '{0.text} - Профиль \n'\
    '{1.text} - Занятия \n'\
    '{2.text} - Экзамены \n'\
    '{3.text} - Расписание преподавателя'.format(
        
        profile_button, lessons_button, 
        exams_button, tutors_info_button
        
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

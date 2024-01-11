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
    '{3.text} - Изменить группу'
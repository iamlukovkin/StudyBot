from telebot.types import InlineKeyboardButton


profile_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="👤", 
    callback_data="profile"

)

lessons_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📓", 
    callback_data="lessons"
    
)

exams_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📝", 
    callback_data="exams"
    
)

tutors_info_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="👨‍🦰", 
    callback_data="tutors"
    
)

update_database_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="Обновить базу данных", 
    callback_data="update_database"
    
)

homepage_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="🏠",
    callback_data="homepage"

)

edit_name_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="🖊",
    callback_data="edit_name"
    
)

edit_group_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="✏️",
    callback_data="edit_group"
    
)

back_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="◀️",
    callback_data="homepage"

)

student_lessons_today_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📗",
    callback_data="student_lessons_today"
)

student_lessons_tomorrow_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📘",
    callback_data="student_lessons_tomorrow"
)

student_lessons_all_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📚",
    callback_data="student_lessons_all"
    
)

tutor_lessons_today_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📘",
    callback_data="tutor_lessons_today"
    
)

tutor_lessons_tomorrow_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📗",
    callback_data="tutor_lessons_tomorrow"
)

tutor_lessons_all_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📚",
    callback_data="tutor_lessons_all"
    
)

change_mode_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="🔒",
    callback_data="change_mode"
)

support_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📞",
    callback_data="support"
)

stud_tutor_today_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="👨‍🦰",
    callback_data="stud_tutor_today"
)

stud_tutor_tomorrow_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="🕞",
    callback_data="stud_tutor_tomorrow"
)

stud_tutor_all_button: InlineKeyboardButton = InlineKeyboardButton(
    
    text="📑",
    callback_data="stud_tutor_all"
)
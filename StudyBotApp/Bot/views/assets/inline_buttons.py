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
    
    text="◀️ Назад",
    callback_data="homepage"

)
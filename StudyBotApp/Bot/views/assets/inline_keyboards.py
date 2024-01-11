from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from .inline_buttons import *

home_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [
            
            profile_button, 
            lessons_button, 
            exams_button,
            tutors_info_button
            
        ],
        
    ]
    
)

admin_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [
            
            profile_button, 
            lessons_button, 
            exams_button,
            tutors_info_button
            
        ],
        
        [update_database_button]
        
    ]
)

profile_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [
            
            edit_name_button,
            edit_group_button
            
        ],
        [back_button]
    ]
)

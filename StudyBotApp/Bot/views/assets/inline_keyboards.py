from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from .inline_buttons import *

home_student_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [
            
            profile_button, 
            lessons_button, 
            exams_button,
            tutors_info_button
            
        ],
        
    ]
    
)

home_tutor_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [
            
            profile_button, 
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

student_profile_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [edit_name_button, edit_group_button],
        [back_button]

    ]
)

tutor_profile_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        
        [edit_name_button],
        [back_button]

    ]
)

homepage_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[[back_button]]

)

lessons_info_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        [lessons_button, back_button]
    ]
)

tutor_lessons_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        [
            tutor_lessons_today_button, 
            tutor_lessons_tomorrow_button,
            tutor_lessons_all_button],
        [back_button]
    ]
)

student_lessons_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    
    keyboard=[
        [
            student_lessons_today_button, 
            student_lessons_tomorrow_button,
            student_lessons_all_button],
        [back_button]
    ]
)

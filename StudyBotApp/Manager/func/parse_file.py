import os
import Manager
from config import FOLDERS

def _(folder: str, path: str) -> list:
    try:
        files = os.listdir(folder)
    except:
        return []
    
    if 'lessons' in path:
        list_all: list = Manager.find_lessons(folder)
    else:
        list_all: list = Manager.find_exams(folder, FOLDERS['temp'])
    
    return list_all
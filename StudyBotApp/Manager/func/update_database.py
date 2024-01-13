import config
import json
import Manager
from database import *
from datetime import time


def update_lessons(data_list: list) -> tuple[int, int]:
    """
    Updates lessons in database.
    
    Args:
        data_list (list): list of lessons
        
    Returns:
        tuple[int, int]: number of skipped lessons and number of successfully added lessons
    """
    
    session = get_session()
    session.query(Lesson).delete()
    
    for lesson in data_list:
        
        group: str = lesson[0]
        day: str = lesson[1]
        str_time: str = lesson[2]
        week: str = lesson[3]
        lesson_info: str = lesson[4]
        
        list_time = str_time.split('-')
        str_time_start = list_time[0]
        str_time_end = list_time[1] if len(list_time) > 1 else None
        
        times_array: list = [str_time_start, str_time_end]
        db_times: list = []
        
        for el in times_array:
        
            if el is None:
                db_times.append(None)
                continue
        
            for symbol in [':', '.', '-']:
        
                if symbol in el:
                    list_time: list = el.split(symbol)
                    list_time: list = [int(el) for el in list_time]
                    db_times.append(time(list_time[0], list_time[1], 0))
                    break
                
        try: 
            session.add(Lesson(
                group=group, day=day,
                time_start=db_times[0], time_end=db_times[1], 
                week=week, lesson_info=lesson_info))
            session.commit()
        except Exception as e:
            print(e)
        finally:
            session.close()
    
    return len(data_list), len(data_list) - session.query(Lesson).count()


def update_exams(data_list: list) -> tuple[int, int]:
    """
    Updates exams in database.
    
    Args:
        data_list (list): list of exams
    
    Returns:
        tuple[int, int]: number of skipped exams and number of successfully added exams
    """
    
    session = get_session()
    session.query(Session).delete()
    
    for exam in data_list:
        
        group: str = exam[0]
        date: str = exam[1]
        str_time: str = exam[2]
        exam_info: str = exam[3]
        
        for symbol in [':', '.', '-']:
            if symbol in str_time:
                list_time: list = str_time.split(symbol)
                list_time: list = [int(el) for el in list_time]
                break
        
        db_time: time = time(list_time[0], list_time[1], 0)
        
        try: 
            session.add(Session(
                group=group, date=date, 
                time=db_time, exam_info=exam_info))
            session.commit()
        except Exception as e:
            print(e)
        finally:
            session.close()

    return len(data_list), len(data_list) - session.query(Session).count()
        

def _(require_download: bool = False):
    """
    Updates database.
    
    Args:
        require_download (bool, optional): require download. Defaults to False.
        
    Returns:
        tuple[int, int, int, int]: number of skipped lessons, number of successfully added lessons, number of skipped exams, number of successfully added exams
    """
    
    Manager.prepare_database_data(download_files=require_download)
    
    with open(config.FILES['db_data'], 'r') as f:
        data: dict = json.load(f)
        
    for key in data.keys():
        data_list: list = data[key]
        if key == 'lessons':
            lessons_added, lessons_skipped = update_lessons(data_list)
        elif key == 'exams':
            exams_added, exams_skipped = update_exams(data_list)
            
    return lessons_added, lessons_skipped, exams_added, exams_skipped

        
        

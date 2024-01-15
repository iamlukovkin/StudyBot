import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    User model.
    
    :param user_id:
    :param username:
    :param fullanme:
    :param studgroup:
    :param is_admin:
    
    :return:
    """
    __tablename__ = 'users'

    user_id: int = Column(Integer, primary_key=True)
    username: str = Column(String(100), nullable=True, unique=True)
    fullname: str = Column(String(100), nullable=True)
    studgroup: str = Column(String(20), nullable=True)
    is_admin: bool = Column(Boolean, nullable=True, default=False)
    is_tutor: bool = Column(Boolean, nullable=True, default=False)
    
    def get_group(self):
        
        if '_' in self.studgroup:
            my_group: str = self.studgroup.split('_')[1]
            
        else:
            my_group: str = self.studgroup
        
        return my_group
    
    
class Session(Base):
    __tablename__ = 'session'
    
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    group: String = Column(String(20))
    date: Date = Column(String(20))
    time: Time = Column(Time)
    exam_info: Text = Column(Text)
    
    
class Lesson(Base):
    """
    """
    __tablename__ = 'lessons'
    
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    group: String = Column(String(20))
    day: String = Column(String(20))
    time_start: Time = Column(Time)
    time_end: Time = Column(Time, nullable=True)
    week: String = Column(String(20))
    lesson_info: Text = Column(Text)
    
    def get_group(self):
        
        if '_' in self.group:
            my_group: str = self.group.split('_')[1]
            
        else:
            my_group: str = self.group
        
        return my_group
    
    def get_info(self, formatting: bool = True) -> str:
        
        base_date: datetime = datetime.datetime.combine(datetime.date.today(), self.time_start)
        break_time: datetime = base_date + datetime.timedelta(minutes=45)
        break_time: Time = break_time.time()
        
        message_text: str = self.lesson_info + '\n'
        
        if formatting:
            message_text += '\n<b>Начало:</b> {start_time}'
            message_text += '\n<b>Перерыв:</b> {break_time}'
            
            if self.time_end:
                message_text += '\n<b>Конец:</b> {end_time}'
        
        else:
            message_text += '\nНачало: {start_time}'
            message_text += '\nПерерыв: {break_time}' 
            
            if self.time_end:
                message_text += '\nКонец: {end_time}'
            
        
        message_text = message_text.strip() + '\n\n\n'
        
        message_text: str = message_text.format(
            start_time=self.time_start.strftime('%H:%M'),
            break_time=break_time.strftime('%H:%M'),
            end_time=self.time_end.strftime('%H:%M')
        )
        return message_text

    def get_times(self):
        
        base_date: datetime = datetime.datetime.combine(
            datetime.date.today(), self.time_start)
        break_time: datetime = base_date + datetime.timedelta(minutes=45)
        break_time: Time = break_time.time()
        
        return self.time_start, break_time, self.time_end

    def get_info_with_group(self, formatting: bool = True) -> str:
        
        base_date: datetime = datetime.datetime.combine(
            datetime.date.today(), self.time_start)
        break_time: datetime = base_date + datetime.timedelta(minutes=45)
        break_time: Time = break_time.time()
        
        if formatting:
            message_text: str = '<b>({0})</b> {1}\n' 
            message_text += '\n<b>Начало:</b> {2}' 
            message_text += '\n<b>Перерыв:</b> {3}'
            
            if self.time_end:
                message_text += '\n<b>Конец:</b> {4}'
                
        else:
            message_text: str = '({0}) {1}\n' 
            message_text += '\nНачало: {2}' 
            message_text += '\nПерерыв: {3}'
            
            if self.time_end:
                message_text += '\nКонец: {4}\n'
            
        
        message_text: str = message_text.strip() + '\n\n'
        message_text: str = message_text.format(
            self.get_group(),
            self.lesson_info,
            self.time_start.strftime('%H:%M'),
            break_time.strftime('%H:%M'),
            self.time_end.strftime('%H:%M')
        )
        return message_text
    

class Support(Base):
    """ Support model

    Args:
        user_id (int): user id
        time (Time): time
        date (Date): date
        message (Text): message
    """
    __tablename__ = 'support'
    
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer)
    time: Time = Column(Time)
    date: Date = Column(String(20))
    message: Text = Column(Text)
    
    
class RaitingTutor(Base):
    """ RaitingTutor model

    Args:
        id (int): id
        tutor_name (str): tutor name
        count (int): count
    """
    __tablename__ = 'raiting_tutor'
    
    id: Integer = Column(Integer, primary_key=True, autoincrement=True)
    tutor_name: String = Column(String(100))
    count: Integer = Column(Integer)
    
    def increase_count(self):
        self.count += 1
    
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
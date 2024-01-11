from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
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
    
    def get_group(self):
        
        if '_' in self.studgroup:
            my_group: str = self.studgroup.split('_')[1]
            
        else:
            my_group: str = self.studgroup
        
        return my_group
    
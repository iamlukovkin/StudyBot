import sqlalchemy
from sqlalchemy.engine import Engine

import config
from .models import Base


def get_engine() -> Engine:
    
    engine: Engine = sqlalchemy.create_engine(config.db_conn, echo=True)
    
    return engine


def get_session():
    
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    
    return Session()


engine: Engine = get_engine()
Base.metadata.create_all(engine)
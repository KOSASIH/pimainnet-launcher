from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_engine(db_uri):
    return create_engine(db_uri)

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

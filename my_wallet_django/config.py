from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:cheT@localhost:5432/my_wallet'
# DATABASE_URL = 'postgresql://kyioskebqiiols:bfaa60a537021c84f276e122642e47a2f58a102792480561e6a839fc9187284b@ec2-3-213-228-206.compute-1.amazonaws.com:5432/df81ua8gcn4i42'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

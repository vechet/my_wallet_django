from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://postgres:cheT@localhost:5432/my_wallet'
DATABASE_URL = 'postgresql://gytkjiulwanddp:b8aedce7500cc663eadfc3d49713c5d5f9ad05c94cd145973bd9d6c8ba186393@ec2-34-227-135-211.compute-1.amazonaws.com:5432/dfs6u0v2548jqd'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

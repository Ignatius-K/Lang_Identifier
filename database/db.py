import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DB_URL')

engine = create_engine(db_url)
local_session = sessionmaker(autoflush=False, bind=engine)
BASE = declarative_base()



import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

load_dotenv()

Database_URL = os.getenv("DATABASE_URL")


Database_passwd = os.getenv("DATABASE_PASSWD")

engine = create_engine(Database_URL)

metadata = MetaData()

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
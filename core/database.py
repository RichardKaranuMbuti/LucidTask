# core/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
DJANGO_ENV = os.getenv('environment')
print(DJANGO_ENV)

if DJANGO_ENV == 'development':
    DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'db.sqlite3')}"
else:
    DATABASE_USER = os.getenv('db_user')
    DATABASE_PASSWORD = os.getenv('db_password')
    DATABASE_HOST = os.getenv('db_host')
    DATABASE_NAME = os.getenv('db_name')

    DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

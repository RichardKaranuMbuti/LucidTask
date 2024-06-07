# core/init_db.py
from sqlalchemy import create_engine
from database import Base
from models import User, Post
import os

def init_db():
    engine = create_engine(f"sqlite:///{os.path.join(os.path.dirname(__file__), 'db.sqlite3')}")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

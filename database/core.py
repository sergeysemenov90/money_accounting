from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session

load_dotenv()


def get_db_url():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    return f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


engine = create_engine(get_db_url())
session = Session(engine)

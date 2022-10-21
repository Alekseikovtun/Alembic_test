import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from config import db_config
from tables import tables

db = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@localhost:{db_config.POSTGRES_OUT_PORT}/{db_config.DB_NAME}"""

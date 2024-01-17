from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite3 connective - Serverless Database
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# postgres connection
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:MGB12#$5@localhost/TodoApplicationDatabase'

# mysql connection
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:MGB12#$5@127.0.0.1:3306/TodoApplicationDatabase'

# Create Engine for sqlite3
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create Engine for PostgresSQL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create Engine for MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

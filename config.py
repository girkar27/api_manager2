from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy.orm import sessionmaker


DB_URI = 'mysql+pymysql://root:@localhost/empdatabase'
engine = create_engine(DB_URI,echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session();
meta =  MetaData(bind=engine)

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy.orm import sessionmaker
from connectors import config



# DB_URI = 'mysql+pymysql://root:@localhost/employeesdb'
engine = create_engine(config.DB_URI,echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
meta =  MetaData(bind=engine)

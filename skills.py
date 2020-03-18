from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
#import pymysql
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model import Employee

#from sqlalchemy import mysqldb

engine = create_engine(DB_URI,echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session() 
meta =  MetaData(bind=engine)

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    emp_id = Column("emp_id", ForeignKey('employees.id'))
    tech = Column(String(30))     
    employee = relationship("Employee", back_populates='skills')


    def __repr__(self):
        return "Skills(%r %r)" % (self.tech , self.emp_id)


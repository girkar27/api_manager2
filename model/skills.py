# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# #import pymysql
# from sqlalchemy.orm import sessionmaker
# from config import DB_URI, Base 
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model import *
from config import Base, session 


#from sqlalchemy import mysqldb

# engine = create_engine(DB_URI,echo=True)
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session() 
# meta =  MetaData(bind=engine)
class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    emp_id = Column("emp_id", ForeignKey('employees.id'), nullable=False)
    tech = Column(String(30))     
    employees = relationship("model.employees.Employee", back_populates='skills')
    


    def __repr__(self):
        return "Skills(%r %r)" % (self.tech , self.emp_id)

    def commit_skill(self):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            return ("cannot add skills")
# employees.Employee.skills = relationship("Skills", back_populates="employee")
# employees = relationship("Skills", back_populates="employee")


# def commit_user_skill():
#   session.add(self)
#     #session.commit()


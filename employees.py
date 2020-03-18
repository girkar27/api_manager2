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
from skill_table import Skills

#from sqlalchemy import mysqldb

engine = create_engine(DB_URI,echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session() 
meta =  MetaData(bind=engine)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True) 
    firstname = Column(String(30))     
    lastname = Column(String(30))
    age = Column(Integer)    

    def __repr__(self):
        return "Employee(%r %r %r)" % (self.firstname, self.lastname, self.age)

Employee.skills = relationship("Skills", order_by=Skills.id, back_populates="employee")








# j = employees.join(skills, Employee.id==Skills.id)
# stmt = select([Employee]).select_from(j)
# result = conn.execute(stmt)
# result.fetchall()





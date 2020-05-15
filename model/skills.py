# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# #import pymysql
# from sqlalchemy.orm import sessionmaker
# from config import DB_URI, Base 
from model import *
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from mysql import Base, session 



class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    emp_id = Column("emp_id", ForeignKey('employees.id'), nullable=False)
    tech = Column(String(30))     
    employees = relationship("model.employees.Employee", back_populates='skills')
    address_emp_id = relationship("model.address_emp_id.Address_emp_id", back_populates='skills')
    


    def __repr__(self):
        return "Skills(%r %r)" % (self.tech , self.emp_id)

    # def commit_skill(self):
    #     try:
    #         session.add(self)
    #         session.commit()
    #     except Exception as e:
    #         return ("cannot add skills")

def delete_skill_data(skill_obj):
    session.delete(skill_obj)

def get_user_skill(emp_id,tech1):
    user_skill = Skills(emp_id=emp_id, tech=tech1)
    # return user_skill
    session.add(user_skill)
    session.commit()    

def filter_skill_id(id):
    skill_id = session.query(Skills).filter_by(emp_id=id).first()
    return skill_id
    
    # session.commit()
# employees.Employee.skills = relationship("Skills", back_populates="employee")
# employees = relationship("Skills", back_populates="employee")


# def commit_user_skill():
#   session.add(sel00f)
#     #session.commit()


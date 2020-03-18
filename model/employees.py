# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# #import pymysql
# from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model.skills import Skills
from config import DB_URI, Base, session







class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True) 
    firstname = Column(String(30))     
    lastname = Column(String(30))
    age = Column(Integer)
    skills = relationship("Skills", back_populates="employees")   

    def __repr__(self):
        return "Employee(%r %r %r)" % (self.firstname, self.lastname, self.age)


#Employee.skills = relationship("skills.Skills", back_populates="employee")

    def commit_user_details(self):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            return ("cannot commit changes in the database")

        # if firstname.islower():
        #     upper_lastname = lastname.upper(self)
        #session.flush(self)
        # import pdb
        # pdb.set_trace()
    #session.flush()
    









# j = employees.join(skills, Employee.id==Skills.id)
# stmt = select([Employee]).select_from(j)
# result = conn.execute(stmt)
# result.fetchall()





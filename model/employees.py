from model.skills import Skills
from model.address import Address
from model.address_emp_id import Address_emp_id
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship
from mysql import Base, session



class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True) 
    firstname = Column(String(30))     
    lastname = Column(String(30))
    age = Column(Integer)
    skills = relationship("Skills", back_populates="employees")   
    address = relationship("Address", back_populates="employees")   
    address_emp_id = relationship("Address_emp_id", back_populates="employees")   

    def __repr__(self):
        return "Employee(%r %r %r)" % (self.firstname, self.lastname, self.age)


#Employee.skills = relationship("skills.Skills", back_populates="employee")

    # def commit_user_details(self):
    #     try:
    #         session.add(self)
    #         session.commit()
    #     except Exception as e:
    #         return ("cannot commit changes in the database")

def delete_user_data(id):
    session.query(Employee).filter_by(id=id).delete()

    # return x

        

def get_user_details(firstname, lastname, age):
    abc = Employee(firstname=firstname, lastname=lastname, age=age)
    # return abc        
    session.add(abc)    
    session.commit()

def query_id(firstname):
    user_id = session.query(Employee).filter_by(firstname=firstname).first()
    x = user_id.id
    return x    

def fetch_user_id(id):
    a = session.query(Employee).get(id)
    return a

def display_all():
    i = session.query(Employee).all()
    return i
    # import pdb
    # pdb.set_trace()

    # for user in i:


    # session.commit()







# j = employees.join(skills, Employee.id==Skills.id)
# stmt = select([Employee]).select_from(j)
# result = conn.execute(stmt)
# result.fetchall()










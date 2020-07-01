from model import *
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from mysql import Base, session 



class Address_emp_id(Base):
    __tablename__ = 'address_emp_id'
    emp_id = Column("emp_id", ForeignKey('employees.id'), primary_key=True, nullable=False)     
    emp_address = Column("emp_address", ForeignKey('address.emp_address'), nullable=False)
    tech = Column("tech", ForeignKey('skills.tech'), nullable=False)

    employees = relationship("model.employees.Employee", back_populates='address_emp_id')
    skills = relationship("model.skills.Skills", back_populates='address_emp_id')
    address = relationship("model.address.Address", back_populates='address_emp_id')



    def __repr__(self):
        return "Address_emp_id(%r %r %r)" % (self.emp_id, self.emp_address , self.tech)

        

def get_skill_address_data(emp_id, emp_address, tech1):
    skill_address_data = Address_emp_id(emp_id=emp_id, emp_address=emp_address, tech=tech1)
    session.add(skill_address_data)    
    session.commit()


def filter_address_skill_id(id):
    address_skill_id = session.query(Address_emp_id).filter_by(emp_id=id).first()
    return address_skill_id


def delete_add_skill_data(id):
    session.query(Address_emp_id).filter_by(emp_id=id).delete()

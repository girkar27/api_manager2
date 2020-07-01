from model import *
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from mysql import Base, session 


class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True)
    emp_id = Column("emp_id", ForeignKey('employees.id'), nullable=False)
    emp_address = Column(String(30))     
    employees = relationship("model.employees.Employee", back_populates='address')
    address_emp_id = relationship("model.address_emp_id.Address_emp_id", back_populates='address')



    def __repr__(self):
        return "Address(%r %r)" % (self.emp_address, self.emp_id)




def delete_address_data(id):
    session.query(Address).filter_by(emp_id=id).delete()


def get_user_address(emp_id, emp_address):
    user_address =Address(emp_id=emp_id, emp_address=emp_address)
    # return user_skill
    session.add(user_address)
    session.commit()

def filter_address_id(id):
    address_id1 = session.query(Address).filter_by(emp_id=id).first()
    return address_id1

def display_address():
    i= session.query(Address).all()
    return i


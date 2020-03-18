from model.employees import  Employee, Column, Integer, String
#from model.employees import Base, meta, engine, session, Employee, Column, Integer, String
from model.skills import Skills, Column, Integer, String
#from model.skills import Skills, Base, meta, engine, session, Column, Integer, String
import json
from flask_marshmallow import Marshmallow
from flask import request
from config import session


def add_user():
    try:
        #user1 = session.query(Employee).all()
        #user2 = session.query(Skills).all()
        firstname = request.json["firstname"]
        lastname = request.json["lastname"]
        age = request.json["age"]
        skill =request.json["skills"]


        if firstname.islower():
            upper_firstname = firstname.upper()
        if firstname.islower():
            upper_lastname = lastname.upper()
        
        user_details = Employee(firstname=upper_firstname, lastname=upper_lastname, age=age)
        user_details.commit_user_details()
        #session.flush()
        user_id = session.query(Employee).filter_by(firstname=upper_firstname).first()
        for tech in skill:       
            user_skill = Skills(emp_id=user_id.id, tech=skill[tech])
            user_skill.commit_skill()                                                          
        z = {"firstname":upper_firstname,"lastname":upper_lastname, "age":age, "skills":skill["tech"]}
        return z
    except Exception as e:
        return ("invalid entry")

def update(id):
    try:
        a = session.query(Employee).get(id)
        if a != None:
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            # import pdb
            # pdb.set_trace()
            age = request.json['age']
            skills = request.json['skills']

            skill_obj = session.query(Skills).filter_by(emp_id=id).first() 

            if firstname.islower():
                firstname = firstname.upper()   
            if lastname.islower():
                lastname = lastname.upper()
            a.firstname = firstname
            a.lastname = lastname
            a.age = age
            skill_obj.tech=skills['tech']
            session.commit()
            updated_user={"firstname":firstname,"lastname":lastname, "age":age, "skills":skills["tech"]}
            return updated_user


        else:
            return ("UserID incorrect")
    except Exception as e:
        return ("Cannot update entry")
                

def delete_user(id):
    try:
        user = session.query(Employee).get(id)
        user2 = session.query(Skills).filter_by(emp_id=id).first()
        #if user user2  !=None:
        session.delete(user)
        session.delete(user2)
        session.commit()
        final = {"firstname":user.firstname,"lastname":user.lastname}
        return final
    except Exception as e:
        return e
        session.rollback()


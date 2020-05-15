
# from api_flask.model import skills
# from api_flask.model import address
# from api_flask.model import address_emp_id

from model.skills import Skills, get_user_skill, filter_skill_id, delete_skill_data
from model.address import Address, get_user_address, filter_address_id, delete_address_data
from model.address_emp_id import Address_emp_id, get_skill_address_data, filter_address_skill_id, delete_add_skill_data
import json
from flask_marshmallow import Marshmallow
from flask import request
from mysql import session
from model import employees  


    
def add_user():

    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    age = request.json["age"]
    skill =request.json["skills"]
    emp_address =request.json["address"]

    if firstname == "":
        return ("no firstname inserted")
    if lastname == "":
        return ("no lastname inserted")
    if skill == {}:
        return ("no skill inserted")
    if emp_address == {}:
        return ("no address inserted") 


    user1 = employees.get_user_details(firstname,lastname, age)
    user_query_id = employees.query_id(firstname)
    emp_id = user_query_id
    tech1 = skill["tech"]
    # user_id = session.query(employees.Employee).filter_by(firstname=upper_firstname).first()
    x = get_user_skill(emp_id,tech1)
    y = get_user_address(emp_id,emp_address)
    w = get_skill_address_data(emp_id,emp_address, tech1)
    # user_skill = Skills(emp_id=user_id.id, tech=skill['tech'])    
    # user_skill.commit_skill()                                                          
    z = {"firstname":firstname,"lastname":lastname, "age":age, "skills":tech1,"address":emp_address}
    return z
           
  
def update(id):
    
    fetched_id = employees.fetch_user_id(id)
    if fetched_id != None:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        age = request.json['age']
        skills = request.json['skills']
        emp_address =request.json["address"]
        emp_list = [firstname, lastname, age]
        # import pdb
        # pdb.set_trace()

        skill_obj = filter_skill_id(id)
        address_obj = filter_address_id(id)
        address_skill = filter_address_skill_id(id) 

        if emp_address =="":

            fetched_id.firstname = firstname
            fetched_id.lastname = lastname
            fetched_id.age = age
            skill_obj.tech=skills['tech']
            updated_user = {"firstname":firstname,"lastname":lastname, "age":age, "skills":skills['tech']}
            return updated_user

        elif skills =={}:
            fetched_id.firstname = firstname
            fetched_id.lastname = lastname
            fetched_id.age = age
            fetched_id.emp_address = emp_address
            updated_user = {"firstname":firstname,"lastname":lastname, "age":age, "address":emp_address}
            return updated_user     
        else:
            fetched_id.firstname = firstname
            fetched_id.lastname = lastname
            fetched_id.age = age
            skill_obj.tech=skills['tech']
            fetched_id.emp_address = emp_address
            updated_user = {"firstname":firstname,"lastname":lastname, "age":age, "skills":skills['tech'],"address":emp_address}
            return updated_user
        session.commit()
    

                

def delete_user(id):
    
    user = employees.fetch_user_id(id)
    skill_obj = filter_skill_id(id)
    address_obj = filter_address_id(id)
    address_skill_obj = filter_address_skill_id(id) 
    employees.delete_user_data(user)
    delete_skill_data(skill_obj)
    delete_address_data(address_obj)
    delete_add_skill_data(address_skill_obj)
    # import pdb
    # pdb.set_trace()
    final = {"firstname":user.firstname,"lastname":user.lastname, "age":user.age, "skills":skill_obj.tech,"address":address_obj.emp_address}
    return final
    return ('user deleted')





def display_user(id):
    user = employees.fetch_user_id(id)
    skill_obj = filter_skill_id(id)
    address_obj = filter_address_id(id)
    address_skill_obj = filter_address_skill_id(id)
    # import pdb
    # pdb.set_trace()
    if skill_obj ==None:
        final = {"firstname":user.firstname,"lastname":user.lastname, "age":user.age, "address":address_obj.emp_address}
        return final
    elif address_obj ==None:  
        final = {"firstname":user.firstname,"lastname":user.lastname, "age":user.age, "skills":skill_obj.tech} 
        return final
    else:
        final = {"firstname":user.firstname,"lastname":user.lastname, "age":user.age, "skills":skill_obj.tech,"address":address_obj.emp_address}
        return final




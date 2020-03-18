from config import  Base, engine, session
from flask import Flask
import pymysql
from flask import request, jsonify
# from model.skills import Skills,  Column, Integer, String, Base, engine, session


from model.skills import Skills,  Column, Integer, String
from model.employees import  Employee, Column, Integer, String 
import json
from flask_marshmallow import Marshmallow
import pymysql
import logic



#ase.metadata.create_all(engine)


a = Flask(__name__)

#add--------------------------------------------------
@a.route("/", methods=["POST","GET"])
def view():
    result1 = logic.add_user()
    return jsonify(result1)

 #displayy---------------------------------------------   
@a.route("/display", methods=["GET"])
def display():

    results = [{"id":a.id, "firstname":a.firstname,"lastname":a.lastname, "age":a.age} for a in session.query(Employee).all()]
    return jsonify(results)



#update---------------------------------------------------
@a.route("/update/<int:id>", methods=["PUT"])
def update_entry(id):   
    entry = logic.update(id)
    return jsonify(entry)
    





#delete------------------------------------------------------
@a.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    final_delete = logic.delete_user(id)
    return jsonify(final_delete)


#----------------------------------------------skills-------------------------------------------------------------------------------------


if __name__ == "__main__":
    a.run(debug=True)
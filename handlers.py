from mysql import  Base, engine, session
from flask import Flask
import pymysql
from flask import request, jsonify
# from model.skills import Skills,  Column, Integer, String, Base, engine, session


# from model.skills import Skills,  Column, Integer, String
# from model.employees import  Employee, Column, Integer, String 
import json
from flask_marshmallow import Marshmallow
import pymysql
from logic import logic 
from api import a	
from flask import g
from oto import response
# from oto.adaptors.flask import flaskify

# Base.metadata.create_all(engine)


#add--------------------------------------------------
@a.route("/adduser", methods=["POST","GET"])
def view():
    result1 = logic.add_user()

    # import pdb
    # pdb.set_trace()
    return jsonify(result1)
    



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

#display by id----------------------------------------------------------
@a.route("/display/<int:id>", methods=["GET"])
def dislay_by_user(id):
    final_display = logic.display_user(id)
    return jsonify(final_display)


@a.route("/api", methods=["GET"])
def api():
    return {
        "id": 1,
        "name": "jai",
        "age": 30,
        "skills":"python"
    }

@a.route("/display", methods=["GET"])
def display():
    display_one = logic.display_all_users()
    return jsonify(display_one)


# @a.errorhandler(500)
# def exception_handler(error):
#     """Default handler when uncaught exception is raised.

#     Note: Exception will also be sent to Sentry if config.SENTRY is set.

#     Returns:
#         flask.Response: A 500 response with JSON 'code' & 'message' payload.
#     """
#     message = (
#         'The server encountered an internal error '
#         'and was unable to complete your request.')
    
#     return (message)


#----------------------------------------------end-------------------------------------------------------------------------------------

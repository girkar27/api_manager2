 

import json
import unittest
import handlers 
from unittest.mock import MagicMock
from unittest.mock import patch 
from logic import logic
from oto import response
import pytest
# from flask import request
from model import employees
from model import skills
from model import address
from model import address_emp_id


def get_json_output():
    return {
    "firstname":"mamta","lastname":"girkar","age":23,"skills":{"tech":"shipping"},"address":"chembur"}


 
def incomplete_dict():
    return {"lastname":"girkar", "age":22,"skills":"python"}








# def test_add_user(fixture_client):
#     response = fixture_client.post('/', json=get_json_output())

#     # assert response.status_code == 200
#     data = json.loads(response.data.decode()) 
#     import pdb
#     pdb.set_trace()
    # assert data ==  {
    # "firstname":"mamta","lastname":"girkar","age":23,"skills":{"tech":"shipping'"},"address":"chembur"}




def test_update(fixture_client):
    # id = 33
    response = fixture_client.put('/update/1', json=get_json_output())
    data = json.loads(response.data.decode())
    # import pdb
    # pdb.set_trace()
    assert response.status_code == 200
    assert data == {'address': 'chembur', 'age': 23, 'firstname': 'mamta', 'lastname': 'girkar', 'skills': 'shipping'}


 

def test_display_user(fixture_client):
    response = fixture_client.get('/display/2')
    data = json.loads(response.data.decode())
        




















            assert response.status_code == 200
    assert data == {'address': 'ghatkopaassr', 'age': 23, 'firstname': 'aigirkar', 'lastname': 'girkarasasd', 'skills': 'saleasaasdasdasdas'}

    

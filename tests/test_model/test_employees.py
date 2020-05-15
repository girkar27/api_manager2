import pytest
import json
# import requests
import unittest
# import app 
from unittest.mock import MagicMock
from unittest.mock import patch 
# import logic
# from oto import response
import pytest
from model import employees

def status_output():
    return ("firstname", "lastname", "age")



def test_query_id():
    firstname = 'jai'        
    result = employees.query_id(firstname)
    user_id =5
    assert result == user_id


def test_fetch_user_id():
    id = 7
    result = employees.fetch_user_id(id)
    firstname = 'mamta'
    lastname = 'girkar'
    age = 23
    # import pdb
    # pdb.set_trace()
    assert result.firstname == firstname
    assert result.lastname == lastname
    assert result.age == age

    


# def test_fetch_user_id():
#     id = 63
#     result = employees.fetch_user_id(id)
#     # import pdb
#     # pdb.set_trace()
#     firstname = 'HITESH'
#     lastname = 'CHAWDA'
#     age = 23
#     assert  result.firstname == firstname
#     assert result.lastname ==lastname
#     assert result.age ==age







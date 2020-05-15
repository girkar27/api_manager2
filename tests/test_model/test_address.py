import pytest
import json
# import requests
import unittest 
from unittest.mock import MagicMock
from unittest.mock import patch 
# import logic
from oto import response
import pytest
from model import address


def test_filter_address_id():
	id = 7
	result = address.filter_address_id(id)
	# import pdb
	# pdb.set_trace()
	emp_address = 'chembur' 	 		
	assert result.emp_address == emp_address
	assert result.emp_id == id
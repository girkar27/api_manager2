import pytest
import json
import unittest 
from unittest.mock import MagicMock
from unittest.mock import patch 
from oto import response
import pytest
from model import address_emp_id


def test_filter_address_skill_id():
	id = 7
	result = address_emp_id.filter_address_skill_id(id)
	assert result.emp_id == id
	tech = 'pythonpython'
	emp_address = 'chembur'
	assert result.tech ==tech
	assert result.emp_address == emp_address
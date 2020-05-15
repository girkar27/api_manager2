import pytest
import json
# import requests
import unittest 
from unittest.mock import MagicMock
from unittest.mock import patch 
import logic
from oto import response
import pytest
from model import skills



def test_filter_skill_id():
    id = 7
    result = skills.filter_skill_id(id)
    tech = "shipping'"
        
    assert result.tech == tech
    assert result.id == id

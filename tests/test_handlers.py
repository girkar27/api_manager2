import pytest
import json
from flask import request, jsonify
import requests



#     assert 
# def test_list_invaliduser():
# 	rv = fixture_client.post('/', json={"firstname":"jai","lastname":"girkar","age":23 ,"skills":"abc"})
#     json_data = rv.get_json()




def test_display(fixture_client):
	result = fixture_client.get('/display')
	assert result.status_code == 200

def test_view(fixture_client):
	result = fixture_client.get('/')
	assert result.status_code == 200


# def test_add_user_success(
#         mocker, distribution_format_media_types):
#     """Test successful retrieval of distribution_format_media types."""
#     mocker.patch.object(
#         distribution_format_media, 'get_all_media_types',
#         return_value=response.Response(
#             status=200, message=distribution_format_media_types))

#     result = product_configuration.get_distribution_format_media_types()




# def test_list_invaliduser(supply_url):
# 	url = supply_url + "/users/50"
# 	resp = requests.get(url)
# 	assert resp.status_code == 404, resp.text






#@pytest.mark.parametrize("id, firstname, lastname, age",[(1,"Jai","Girkar", 22),(2,"Jaier","Girkarew",25)])
# def test_list_valid_user(supply_url):
# 	url = supply_url
# 	data = {"firstname":"jai","lastname":"girkar","age":23 ,"skills":"abc"}
# 	resp = requests.post(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 200, resp.text
# 	assert j['data']['firstname'] == firstname, resp.text
# 	assert j['data']['lastname'] == lastname, resp.text
# 	assert j['data']['age'] == age, resp.text




# def test_valid_update(supply_url):
# 	url = supply_url + "/update/" + str(id)
# 	data = {"firstname":"newfirstname","lastname":"newlastname","age":23 ,"skills":"newskill"}
# 	resp = requests.get(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 200, resp.text
# 	assert j['user updated'] == "user updated", resp.text



# def test_invalid_update(supply_url):
# 	url = supply_url + "/update/" + int(id) 
# 	data = {}
# 	resp = requests.fixture_client(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 404, resp.text
# 	assert j['error'] == "data not updated", resp.text


# def test_invalid_firstname(supply_url):
# 	url = supply_url + "/update/" + int(id) 
# 	data = {"firstname":,"lastname":"newlastname","age":23 ,"skills":"newskill"}
# 	resp = requests.fixture_client(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 404, resp.text
# 	assert j['error'] == "no firstname inserted", resp.text





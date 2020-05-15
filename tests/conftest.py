import handlers
import pytest
import api


# @pytest.fixture
# def supply_url():
	# return "http://127.0.0.1:5000/"


@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""
    return handlers.a.test_client()


# @pytest.fixture
# def client_headers():
#     x = {"firstname":"jai","lastname":"girkar", "age":22,"skills":"python"}
#     return x





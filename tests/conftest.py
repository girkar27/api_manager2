import pytest
import app


@pytest.fixture
def supply_url():
	return "http://127.0.0.1:5000/"


@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""
    return app.a.test_client()

# @pytest.fixture
# def fixture_client():
#     """Create an api test client fixture."""
#     return a.test_client()

import requests
import pytest


SERVICE_URL = 'https://gorest.co.in/public/v1/users'

@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response

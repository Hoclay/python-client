import os

import pytest

import handwriting


@pytest.fixture
def client():
  API_KEY = os.getenv('API_KEY', 'dev')
  API_SECRET = os.getenv('API_SECRET', 'dev')
  API_URL = os.getenv('API_URL', 'http://docker:3000')
  return handwriting.Client(API_KEY, API_SECRET, base_url=API_URL)


@pytest.fixture
def test_handwriting(client):
  hws = client.list_handwritings({'limit': 1})
  return hws[0]

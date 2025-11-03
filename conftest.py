import pytest
from endpoints.delete_object import DeleteObject
from endpoints.create_object import CreateObject
import random


@pytest.fixture(scope="session")
def base_url():
    return 'https://api.restful-api.dev/objects'


@pytest.fixture
def payload():
    random_num = random.randint(1000, 10000)
    return {
   "name": f"Apple MacBook Pro 16_{random_num}",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}


@pytest.fixture
def obj_id():
    create_object = CreateObject()
    payload = {
       "name": "Apple MacBook Pro 16",

       "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
       }
    }
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_object(create_object.response_json['id'])





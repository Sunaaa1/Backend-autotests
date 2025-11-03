import allure
import requests
from endpoints.base_endpoint import Endpoint

base_url = 'https://api.restful-api.dev/objects'

class CreateObject(Endpoint):
    @allure.step("Создаем новый объект")
    def new_object(self, payload):
        self.response = requests.post(base_url, json=payload)
        self.response_json = self.response.json()

    @allure.step("Проверяем, что имя объекта совпадает с payload")
    def check_name(self, name):
        assert self.response_json["name"] == name
import allure
import requests
from endpoints.base_endpoint import Endpoint

base_url = 'https://api.restful-api.dev/objects'

class GetObject(Endpoint):
    @allure.step("Получаем айди объекта")
    def get_by_id(self, obj_id):
        self.response = requests.get(f"{base_url}/{obj_id}")
        self.response_json = self.response.json()

    @allure.step("Проверяем айди объекта")
    def check_response_id(self, obj_id):
        assert self.response_json["id"] == obj_id
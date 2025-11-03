import allure
import requests
from endpoints.base_endpoint import Endpoint

base_url = 'https://api.restful-api.dev/objects'

class DeleteObject(Endpoint):
    @allure.step("Удаляем объект")
    def delete_object(self, obj_id):
        self.response = requests.delete(f'{base_url}/{obj_id}')
        self.response_json = self.response.json()
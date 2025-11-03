import allure
import requests
from endpoints.base_endpoint import Endpoint

base_url = 'https://api.restful-api.dev/objects'

class UpdateObject(Endpoint):
    @allure.step("Обновляем объект")
    def update_object(self, obj_id, payload):
        updated_payload = payload.copy()
        updated_payload["name"] = 'new name'
        self.response = requests.put(f'{base_url}/{obj_id}', json=updated_payload)
        self.response_json = self.response.json()

    @allure.step("Проверяем обновление данных объекта")
    def check_updated_payload(self):
        assert self.response_json["name"] == "new name"



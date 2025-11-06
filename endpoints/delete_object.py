import allure
import requests
from jsonschema import validate

from endpoints.base_endpoint import Endpoint
from schemas.delete_object_schema import delete_object_schema

base_url = 'https://api.restful-api.dev/objects'

class DeleteObject(Endpoint):
    @allure.step("Удаляем объект")
    def delete_object(self, obj_id):
        self.response = requests.delete(f'{base_url}/{obj_id}')
        self.response_json = self.response.json()

    @allure.step("Валидируем JSON-ответ по схеме delete_object_schema")
    def validate_response_schema(self):
        validate(instance=self.response_json, schema=delete_object_schema)
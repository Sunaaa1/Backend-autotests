import allure
import requests
from jsonschema import validate

from endpoints.base_endpoint import Endpoint
from schemas.get_object_schema import get_object_schema

base_url = 'https://api.restful-api.dev/objects'

class GetObject(Endpoint):
    @allure.step("Получаем айди объекта")
    def get_by_id(self, obj_id):
        self.response = requests.get(f"{base_url}/{obj_id}")
        self.response_json = self.response.json()

    @allure.step("Проверяем айди объекта")
    def check_response_id(self, obj_id):
        assert self.response_json["id"] == obj_id

    @allure.step("Валидируем JSON-ответ по схеме get_object_schema")
    def validate_response_schema(self):
        validate(instance=self.response_json, schema=get_object_schema)
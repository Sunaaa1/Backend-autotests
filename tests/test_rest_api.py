import allure
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from conftest import *


@allure.epic("REST API Tests")
@allure.feature("Objects CRUD")
@allure.story("Create Object")
@allure.title("Создание нового объекта через POST запрос")
def test_create_object(payload):
    with allure.step("Отправляем POST запрос для создания объекта"):
        new_object_endpoint = CreateObject()
        new_object_endpoint.new_object(payload)

    with allure.step("Проверяем статус-код и имя созданного объекта"):
        new_object_endpoint.check_response_is_200()
        new_object_endpoint.check_name(payload["name"])


@allure.epic("REST API Tests")
@allure.feature("Objects CRUD")
@allure.story("Update Object")
@allure.title("Обновление объекта через PUT запрос")
def test_update_object(obj_id, payload):
    with allure.step("Отправляем PUT запрос для обновления объекта"):
        new_object_endpoint = UpdateObject()
        new_object_endpoint.update_object(obj_id, payload)

    with allure.step("Проверяем статус-код и что данные совпадают с payload"):
        new_object_endpoint.check_response_is_200_and_204()
        new_object_endpoint.check_updated_payload()


@allure.epic("REST API Tests")
@allure.feature("Objects CRUD")
@allure.story("Get Object")
@allure.title("Получение объекта через GET запрос")
def test_get_object(obj_id):
    with allure.step("Отправляем GET запрос для получения объекта"):
        new_object_endpoint = GetObject()
        new_object_endpoint.get_by_id(obj_id)

    with allure.step("Проверяем статус-код и ID полученного объекта"):
        new_object_endpoint.check_response_is_200()
        new_object_endpoint.check_response_id(obj_id)


@allure.epic("REST API Tests")
@allure.feature("Objects CRUD")
@allure.story("Delete Object")
@allure.title("Удаление объекта через DELETE запрос")
def test_delete_object(obj_id):
    with allure.step("Отправляем DELETE запрос для удаления объекта и проверяем статус код 200"):
        new_object_endpoint = DeleteObject()
        new_object_endpoint.delete_object(obj_id)
        new_object_endpoint.check_response_is_200()

    with allure.step("Отправляем GET запрос по ID удаленного объекта и проверяем что объект действительно удален"):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(obj_id)
        get_object_endpoint.check_response_is_404()


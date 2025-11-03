import allure


class Endpoint:
    response = None
    response_json = None


    @allure.step("Проверяем, что ответ содержит статус 200")
    def check_response_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Проверяем, что ответ содержит статус 200/204")
    def check_response_is_200_and_204(self):
        assert self.response.status_code in (200, 204)

    @allure.step("Проверяем, что ответ содержит статус 404")
    def check_response_is_404(self):
        assert self.response.status_code == 404
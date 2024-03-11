import pytest
import json
from utils.api import Test_place

class Test_users():
    # Фикстура для начала тестовой сессии
    @pytest.fixture(scope='session')
    def setup(self):
        print("Начало тестовой сессии")
        yield
        print("Конец тестовой сессии")

    # Фикстура для запуска и завершения каждого теста
    @pytest.fixture(scope='function')
    def set_setup(self):
        print("тест запущен")
        yield
        print("тест завершен")

    @pytest.mark.parametrize("page_number", [1, 2, 3])  # Параметризация для страниц 1, 2 и 3
    def test_get_parametrize(self, set_setup, page_number):
        """
        Параметризованный тест для метода `metod_get`.
        Проверяет ответ сервера на запрос с разными номерами страниц.
        """
        test_place_get = Test_place()
        response = test_place_get.metod_get(page_number)
        assert response.status_code == 200

        json_response = json.loads(response.text)
        assert json_response['page'] == page_number

    def test_post(self, set_setup):
        """
        Тест для метода POST.
        Проверяет ответ сервера на запрос с использованием метода POST.
        """
        print("Метод POST")
        test_place_instance_post = Test_place()
        response = test_place_instance_post.metod_post()
        assert response.status_code == 200

    def test_get(self, set_setup):
        """
        Тест для метода GET.
        Проверяет ответ сервера на запрос с использованием метода GET.
        """
        test_place_instance_get = Test_place()
        response = test_place_instance_get.metod_get(None)
        assert response.status_code == 200

    def test_put(self, set_setup):
        """
        Тест для метода PUT.
        Проверяет ответ сервера на запрос с использованием метода PUT.
        """
        test_place_instance_put = Test_place()
        response = test_place_instance_put.metod_put()
        assert response.status_code == 200

    def test_delete(self, set_setup):
        """
        Тест для метода DELETE.
        Проверяет ответ сервера на запрос с использованием метода DELETE.
        """
        test_place_instance_delete = Test_place()
        response = test_place_instance_delete.metod_delete()
        print(response)
        assert response.status_code == 204

    def test_json_data(self, set_setup):
        """
        Тест для проверки данных в формате JSON.
        """
        test_place_instance_get = Test_place()
        response = test_place_instance_get.metod_get(None) #использовал метод гет для вызова тела ответа
        json_response = json.loads(response.text)
        # Проверка наличия ключей 'page', 'per_page', 'total', 'total_pages'
        assert 'page' in json_response
        assert 'per_page' in json_response
        assert 'total' in json_response
        assert 'total_pages' in json_response

        # Проверка наличия ключей 'id', 'email', 'first_name', 'last_name', 'avatar' в каждом элементе списка 'data'
        if 'data' in json_response:
            for user in json_response['data']:
                assert 'id' in user
                assert 'email' in user
                assert 'first_name' in user
                assert 'last_name' in user
                assert 'avatar' in user
        else:
            assert False, "JSON-ответ не содержит списка пользователей 'data'"

    @pytest.mark.parametrize("page_number", [1, 2, 3])  # Параметризация для страниц 1, 2 и 3
    def test_json(self, set_setup, pytestconfig, page_number):
        """
        Тест для проверки данных в формате JSON с параметризацией.
        """
        logs_enabled = pytestconfig.getoption("logs")
        print("Logging enabled:", logs_enabled)

        test_place_instance_get = Test_place()
        response = test_place_instance_get.metod_get(page_number=page_number)
        assert response.status_code == 200

        json_response = json.loads(response.text)
        assert json_response['page'] == page_number
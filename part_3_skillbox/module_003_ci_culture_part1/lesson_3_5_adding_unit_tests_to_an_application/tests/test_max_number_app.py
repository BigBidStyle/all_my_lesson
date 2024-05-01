import unittest

from lesson_3_5_adding_unit_tests_to_an_application.max_number_app import app

class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/max_number/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        numbers = 1, 2
        url = self.base_url + '/'.join(str(i) for i in numbers) # Создаем URL
        response = self.app.get(url)    # Отправляем запрос
        response_text = response.data.decode() # Получаем ответ
        correct_answer_str = f'<i>{max(numbers)}</i>'   # Ответ должен быть таким...
        self.assertTrue(correct_answer_str in response_text)
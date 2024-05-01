import unittest  # Библиотека тестирования Unit = (нижний уровень кода)
from lesson_3_3_unit_testing_on_practica.social_age import get_social_status

class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        expected_res = 'ребенок'
        function_res = get_social_status(age)
        self.assertEquals(expected_res, function_res)   # Функция проверяет равенство значений.


    # Проверь, что появилось исключение ValueError, если оно появилось, то тест пройден иначе будет тест не пройден.
    # Пример использования может быть такой...
    # Что если покупатель купил товара больше чем есть на складе...
    def test_cannot_pass_str_as_age(self):
        age = "8"
        with self.assertRaises(ValueError):
            get_social_status(age)
import unittest

from lesson_3_5_adding_unit_tests_to_an_application.good_days_app import app

class TestGoodDayApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/good_days/'

    def test_good_days_app(self):
        user_name = "username"
        response = self.app.get(self.base_url + user_name)
        response_text = response.data.decode()
        self.assertTrue(user_name in response_text)
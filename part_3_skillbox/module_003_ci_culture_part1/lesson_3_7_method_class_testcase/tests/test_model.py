import time
from unittest import TestCase, main
class PerformanceTest(TestCase):
    file = None

    @classmethod
    def setUpClass(cls): # <-- Метод вызывается перед запуском всех тестов в этом классе. Он позволяет задать общие
        # настройки и открыть ресурсы, которые будут использованы всеми тестами.
        cls.file = open("test_log.txt", "a")

    def setUp(self):# <-- Метод вызывается перед запуском каждого теста и позволяет не писать один и тот же код
        # по созданию экземпляра тестируемого класса.
        self.start = time.perf_counter() # <-- возвращает текущее время с наибольшим доступным разрешением.

    def test_million_appends(self):
        N = 1000000
        lst = []
        [lst.append(i) for i in range(N)]
        self.assertListEqual(lst, list(range(N)))

    def test_sum_of_numbers(self):
        N = 1000000
        self.assertEqual(sum(range(N + 1)), N * (N + 1) // 2)

    def tearDown(self): # <-- Метод вызывается после завершения всех тестов в этом классе. Он позволяет закрыть
        # ресурсы, которые были открыты в setUpClass. А также очистить данные, созданные в результате тестирования.
        self.end = time.perf_counter()
        # self.id() выдаст название текущего теста в таком формате: __main__.PerformanceTest.test_million_appends
        print(self.id(), self.end - self.start, file=self.file)

    @classmethod
    def tearDownClass(cls):
        cls.file.close()

if __name__ == '__main__':
    main()
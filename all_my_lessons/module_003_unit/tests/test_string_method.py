import unittest
class CalculationTest(unittest.TestCase):   # Математический метод.

    def test_plus(self):
        self.assertEqual((2+2), 4)

    def test_minus(self):
        self.assertEqual((3+1), 4)

    def test_multi(self):
        self.assertEqual((2*4), 8)

    def test_divide(self):
        self.assertEqual((9/3), 3)


class TestStringMethods(unittest.TestCase): # <-- Строковой метод.

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # проверьте, что s.split завершается неудачно, если разделитель не является строкой
        with self.assertRaises(TypeError):
            s.split(2)

class DefaultWidgetSizeTestCase(unittest.TestCase): # Тестовый пример размера виджета по умолчанию
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

if __name__ == '__main__':
    unittest.main()
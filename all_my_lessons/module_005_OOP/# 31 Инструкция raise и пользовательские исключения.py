class ExceptionPrint(Exception):
    """Общий класс исключения принтера."""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.massage = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.massage}'

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не печатает')

    def send_to_print(self, data):
        return False

p = PrintData()
try: p.send_data('1,2,3')
except ExceptionPrintSendData:
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати')


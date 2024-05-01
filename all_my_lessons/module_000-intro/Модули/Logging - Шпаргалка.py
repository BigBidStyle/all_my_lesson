import logging
logging.warning('Watch out!') # <-- Вывод сообщения на экран.

logging.basicConfig(filename="log.txt", level = logging.INFO)
try:
    print(10 / 0)
except Exception as error:
    logging.error(str(error))

logging.basicConfig(level = logging.DEBUG)

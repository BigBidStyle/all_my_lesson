# Очереди Queue и LifoQueue
# Мы рассмотрим две самые популярные и полезные реализации очереди: Queue и LifoQueue.

# В документации вы можете узнать об остальных очередях.

# Модуль queue
# Установка: модуль queue также является встроенным модулем Python, поэтому нет необходимости в его дополнительной
# установке.

# Подключение: вы можете импортировать классы очередей, например, с помощью

# from queue import Queue, LifoQueue

# * Ниже будет использован термин «потокобезопасность».

# Вы ещё не рассматривали тему многопоточного программирования, но это является важным преимуществом данных коллекций,
# поэтому стоит вернуться к ней ещё раз после изучения многопоточности.

# Queue
# Queue из модуля queue представляет собой осуществление потокобезопасной очереди (queue) в Python. Она реализует
# принцип First-In/First-Out (FIFO), «первый вошёл — первый вышел», то есть работает как обычная, привычная вам,
# очередь (пришёл в магазин, встал в начало очереди — первым купил товар, встал в конец очереди — последним купил
# товар).

# Этот класс предоставляет методы для добавления и удаления элементов из очереди и может использоваться для
# синхронизации данных между потоками в многопоточных приложениях.
# Некоторые основные аспекты и примеры использования Queue:

from queue import Queue
# Создание экземпляра очереди
q = Queue()
# Добавление элементов в очередь
q.put(1)
q.put(2)
q.put(3)
# Получение и удаление элемента из очереди
item = q.get()
print(item) # Вывод: 1

# Проверка, пуста ли очередь
is_empty = q.empty()
print(is_empty) # Вывод: False

# Получение размера очереди
size = q.qsize()
print(size) # Вывод: 2

# Очистка очереди
q.queue.clear()

# # Проверка, пуста ли очередь после очистки
is_empty = q.empty()
print(is_empty) # Вывод: True
# Важно отметить, что Queue из модуля queue является реализацией очереди, а не стека. Если вам нужен стек, можете
# использовать LifoQueue, который вы рассмотрите ниже.
# --------------------------------------------------------------------------------------------------------------------#
# LifoQueue
# LifoQueue из модуля queue представляет реализацию стека (стека по принципу Last-In/First-Out (LIFO), или «последний
# вошёл, первый вышел»).
# Он предоставляет методы для добавления и удаления элементов из стека.
# Посмотрите на ключевые аспекты и примеры использования LifoQueue:
print("----------------------")
from queue import LifoQueue

# Создание экземпляра стека
stack = LifoQueue()

# Добавление элементов в стек
stack.put(1)
stack.put(2)
stack.put(3)

# Получение и удаление элемента из стека
item = stack.get()
print(item) # Вывод: 3

# Проверка, пуст ли стек
is_empty = stack.empty()
print(is_empty) # Вывод: False

# Получение размера стека
size = stack.qsize()
print(size) # Вывод: 2

# Очистка стека
stack.queue.clear()

# Проверка, пуст ли стек после очистки
is_empty = stack.empty()
print(is_empty) # Вывод: True
# LifoQueue предоставляет функциональность стека, где последний добавленный элемент будет первым удалённым
# (LIFO: Last-In/First-Out). Вы можете добавлять элементы в стек при помощи метода put и получать их при помощи
# метода get.

# Важно отметить, что LifoQueue реализует именно структуру данных стека.

# Вы можете заметить, что между Queue и LifoQueue нет большой разницы, и вы будете правы, но эта разница имеет
# ключевое значение, из-за неё каждая структура используется для своих задач.

# Примеры задач, которые решаются при помощи стека:

# Редактор текста с отменой и повтором действий.
# Редакторы текста часто используют стек для реализации функциональности отмены (undo) и повтора (redo) действий.
# Каждое выполненное действие помещается в стек, и пользователь может отменить или повторить последние действия,
# извлекая их из стека.
# Обработка вызовов функций.
# Во время выполнения программы стек может использоваться для управления вызовами функций. Каждый раз при вызове
# функции информация о нём помещается в стек и извлекается из стека, когда функция завершается, чтобы вернуться к
# предыдущему контексту выполнения.
# Примеры задач, которые решаются при помощи очереди:

# Обработка задач веб-сервером.
# Веб-серверы обычно используют очередь для управления запросами от клиентов. Поступившие запросы помещаются в очередь,
# а сервер обрабатывает их в порядке получения. Это обеспечивает справедливое распределение ресурсов и обработку
# запросов в порядке очерёдности.
# Кеширование данных.
# Очередь может использоваться для кеширования данных в системе, наиболее актуальные данные которой хранятся в начале
# очереди, а более старые — в конце. При достижении максимального размера очереди старые данные будут автоматически
# удаляться, чтобы освободить место для новых.
# Обработка задач в фоновом режиме.
# Очередь может использоваться для обработки задач в фоновом режиме, например отправки электронных писем или обработки
# длинных вычислений. Задачи помещаются в очередь, а отдельный процесс или поток обрабатывает их по мере доступности
# ресурсов.
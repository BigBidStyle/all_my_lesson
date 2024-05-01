"""https://docs.wxpython.org"""

import wx
app = wx.App() # <- Инициализация приложения.

frame = wx.Frame(None, title = 'Hello Water-Wave', style = wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|
                         wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN, size= (600, 400), pos = (-10, 0))
frame.Show()  # <-- Вывести окно на экран.

app.MainLoop()

# App <- Класс общего функционала приложения.
# Frame <- Класс отдельного окна (их может быть несколько).


# wx.Frame(parent, id=-1, title=", pos = wx.DefaultPosition, size=wz.DefaultSize, style = wx.DEFAULT_FRAME_STYLE,
# name= 'frame')

# Parent <-- Ссылка на родительское окно с которым связан данный фрейм. (Если мы создаем одно главное окно,
# то значение ставим None.

# id <-- id данного фрейма.
# title <-- Заголовок
# pos <--  Позиция данного окна.
# size <-- Размер данного окна.
# style <-- Стиль
# wx.DEFAULT_FRAME_STYLE = (wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|
#                          wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)

# wx.MINIMIZE_BOX <-- Кнопка для свертывания окна.
# wx.MAXIMIZE_BOX <-- Кнопка для распахивания окна.
# wx.RESIZE_BORDER <-- Делаем окно с изменяемыми размерами.
# wx.SYSTEM_MENU <-- Разрешаем системное меню.
# wx.CAPTION <-- Разрешаем заголовок у окна.
# wx.CLOSE_BOX <-- Кнопка закрытия окна.
# wx.CLIP_CHILDREN <--
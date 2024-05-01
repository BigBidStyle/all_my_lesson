import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        panel = wx.Panel(self) # <-- Создаем панель.
        vbox = wx.BoxSizer(wx.VERTICAL) # <-- Создаем Бокс сайзер в котором будем размещать элементы вертикально.

        # Параметры...
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)
        # ------------------------------------------------------------------------------------------------------------ #
        # Сайзер 1
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) # <-- Создаем горизонтальный сайзер.

        st1 = wx.StaticText(panel, label="Путь к файлу: ") # <-- Создаем текстовый элемент.
        tc = wx.TextCtrl(panel) # <-- Создаем элемент поле ввода текста.

        hbox1.Add(st1, flag=wx.RIGHT, border=8) # <-- В сайзере размещаем элемент с отступом справа в 8 пикселей.
        hbox1.Add(tc, proportion=1) # <-- В сайзере размещаем элемент с заполнением всего пространства.

        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10) # <-- Размещаем созданный сайзер в
        # бокс-сайзер.
        # ------------------------------------------------------------------------------------------------------------ #
        # Сайзер 2
        st2 = wx.StaticText(panel, label="Содержимое файла: ") # <-- Создаем текстовый элемент.
        vbox.Add(st2, flag=wx.EXPAND|wx.ALL, border=10) # <-- Размещаем созданный элемент в бокс-сайзере.
        # ------------------------------------------------------------------------------------------------------------ #
        # Сайзер 3
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)  # <-- Создаем элемент поле ввода текста.
        vbox.Add(tc2, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)  # <-- Размещаем созданный
        # Сайзер в бокс-сайзере.
        # ------------------------------------------------------------------------------------------------------------ #

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)  # <-- Создаем горизонтальный сайзер.

        # Создаем пару кнопок.
        button_ok = wx.Button(panel, label="Yes", size=(70, 30))
        button_no = wx.Button(panel, label="No", size=(70, 30))

        hbox2.Add(button_ok, flag=wx.LEFT, border=10)
        hbox2.Add(button_no, flag=wx.LEFT, border=10)

        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, border=10)
        panel.SetSizer(vbox)


app = wx.App()  # <- Инициализация приложения.
ex = MyFrame(None, 'wxPython')  # - Мое окошко.
ex.Show()   # <-- Вывести окно на экран.
app.MainLoop()  # <-- Главный цикл обработки событий.



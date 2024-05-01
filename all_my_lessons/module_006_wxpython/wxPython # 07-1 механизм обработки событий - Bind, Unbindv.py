# wx.EVT_BUTTON - Событии, генерируемое виджетом wx.Button.
# wx.EVT_MENU - Событии, генерируемое меню.
# wx.EVT_TEXT - Событии, генерируемое wx.TextCtrl.
# wx.EVT_TOOL - Событии, генерируемое toolbox.
# wx.EVT_MOVE - Событии, при перемещение окна.
# wx.EVT_PAINT - Событии, при перерисовки элемента (обычно окна).
# wx.EVT_KEW_DOWN -Событии, при нажатии клавишу.
# wx.EVT_KEY_UP - Событие при отпускании кнопки.


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        btn1 = wx.Button(self, wx.ID_ANY, "Key 1")
        btn2 = wx.Button(self, wx.ID_ANY, "Key 2")
        btn1.SetPosition(wx.Point(10,10))
        btn2.SetPosition(wx.Point(200,10))

        # Один из вариантов указания ID - действия
        # self.Bind(wx.EVT_BUTTON, self.onButton1, id=btn1.GetId())
        # self.Bind(wx.EVT_BUTTON, self.onButton2, id=btn2.GetId())

        # Или воспользоваться таким вариантом.
        self.Bind(wx.EVT_BUTTON, self.onButton1, btn1)
        self.Bind(wx.EVT_BUTTON, self.onButton2, btn2)


    def onButton1(self, event,):
        print("Нажатие на key 1")

    def onButton2(self, event):
        print("Нажатие на key 2")

def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
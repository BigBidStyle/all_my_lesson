import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        panel =wx.Panel(self)
        btn = wx.Button(panel, wx.ID_ANY, "Key 1")

        btn.Bind(wx.EVT_BUTTON, self.onButton)
        panel.Bind(wx.EVT_BUTTON, self.onButtonPanel)
        self.Bind(wx.EVT_BUTTON, self.onButtonFrame)

        panel.Unbind(wx.EVT_BUTTON) # <-- Сброс обработчика
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)


    def onCloseWindow(self, event):
        dial = wx.MessageDialog(None, "Вы действительно хотите выйти?", "Вопрос", wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
        ret = dial.ShowModal()  # <-Выводим диалог

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

    def onButton(self, event):
        print("Уровень кнопки.")
        event.Skip() # <- Указываем, чтобы данное событие распространялось дальше к родительским элементам.

    def onButtonPanel(self, event):
        print("Уровень панели.")
        event.Skip()

    def onButtonFrame(self, event):
        print("Уровень окна.")


def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
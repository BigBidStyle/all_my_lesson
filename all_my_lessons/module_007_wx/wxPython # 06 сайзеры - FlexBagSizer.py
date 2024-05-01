import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        panel = wx.Panel(self)


        gr = wx.GridBagSizer(5, 5) # Cетка 5*5
        text = wx.StaticText(panel, label="Email:")
        gr.Add(text, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border = 5)

        tc = wx.TextCtrl(panel)
        gr.Add(tc, pos=(1,0), span=(1, 5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border = 3)
        # span(1, 5) для второго столбца будем обхватывать пять столбцов

        # Создаем пару кнопок.
        button_ok = wx.Button(panel, label="Yes", size=(120, 24))
        button_no = wx.Button(panel, label="No", size=(120, 24))
        gr.Add(button_ok, pos=(3, 3))
        gr.Add(button_no, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=3)

        gr.AddGrowableCol(1)
        gr.AddGrowableRow(2)
        panel.SetSizer(gr)
def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
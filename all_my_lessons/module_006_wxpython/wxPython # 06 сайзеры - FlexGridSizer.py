import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        hbox = wx.BoxSizer()

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(4, 2, 10 ,10)

        fb.AddMany([(wx.StaticText(panel, label="Ф.И.О.:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="email:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="Адрес:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="О себе:")),
                    (wx.TextCtrl(panel, style=wx.NB_MULTILINE), wx.ID_ANY, wx.EXPAND)])



        # FlexGridSizer.AddGrowableCol(self, col, proportion=0)
        fb.AddGrowableCol(1,1)
        # FlexGridSizer.AddGrowableRow(self, row, proportion=0)
        fb.AddGrowableRow(3, 1)

        hbox.Add(fb, proportion= 1, flag=wx.EXPAND|wx.ALL, border=3)
        panel.SetSizer(hbox)

def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
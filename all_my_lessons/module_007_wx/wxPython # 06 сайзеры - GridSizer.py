import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL) # <- Сайзер.

        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        gbox = wx.GridSizer(1,4,5,5)
        gbox.AddMany([(wx.Button(panel, label='Cls'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='Bck'), 0, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='Close'), 0, wx.EXPAND),
                      (wx.Button(panel, label='7'), 0, wx.EXPAND),
                      (wx.Button(panel, label='8'), 0, wx.EXPAND),
                      (wx.Button(panel, label='9'),0, wx.EXPAND),
                      (wx.Button(panel, label='/'), 0, wx.EXPAND),
                      (wx.Button(panel, label='4'), 0, wx.EXPAND),
                      (wx.Button(panel, label='5'), 0, wx.EXPAND),
                      (wx.Button(panel, label='6'), 0, wx.EXPAND),
                      (wx.Button(panel, label='*'), 0, wx.EXPAND),
                      (wx.Button(panel, label='1'), 0, wx.EXPAND),
                      (wx.Button(panel, label='2'), 0, wx.EXPAND),
                      (wx.Button(panel, label='3'), 0, wx.EXPAND),
                      (wx.Button(panel, label='-'), 0, wx.EXPAND),
                      (wx.Button(panel, label='0'), 0, wx.EXPAND),
                      (wx.Button(panel, label='.'), 0, wx.EXPAND),
                      (wx.Button(panel, label='='), 0, wx.EXPAND),
                      (wx.Button(panel, label='+'), 0, wx.EXPAND)
                       ])

        vbox.Add(gbox, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        panel.SetSizer(vbox) # <-- Запускаем в главном окне сайзер.




def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
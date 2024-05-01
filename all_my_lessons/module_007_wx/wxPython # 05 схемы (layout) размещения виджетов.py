import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title, size=(600, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer() # <- Сайзер.
        # В кавычках можно указать расположение виджетов
        # wx.VERTICAL <-- Флаг, для расположения виджетов на панели.

        # img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("pic_1.jpg")) # <- Загружаем картинку.
        # img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("windows.jpg")) # <- Загружаем картинку.

        # img1.SetPosition((10, 10)) # <-- Абсолютное позиционирование(координаты размещения картинки).
        # img2.SetPosition((300, 40)) # <-- Абсолютное позиционирование(координаты размещения картинки).

        # vbox.Add(img1, wx.ID_ANY, wx.EXPAND) # <-- Добавляем виджет в сайзер.
        # vbox.Add(img2, wx.ID_ANY, wx.EXPAND) # <-- Добавляем виджет в сайзер.
        # wx.EXPAND <-- Распахнуть ячейку на всю доступную область.

        mp = wx.Panel(panel)
        mp.SetBackgroundColour("#ffffe5")
        vbox.Add(mp, wx.ID_ANY, wx.EXPAND|wx.ALL, 10)
        # wx.EXPAND|wx.ALL, 10  <-- Сделать со всех четырех сторон отступы в 20 пикселей
        panel.SetSizer(vbox) # <-- Запускаем в главном окне сайзер.


def main():
    app = wx.App()  # <- Инициализация приложения.
    ex = MyFrame(None, 'wxPython')  # - Мое окошко.
    ex.Show()   # <-- Вывести окно на экран.
    app.MainLoop()  # <-- Главный цикл обработки событий.


if __name__ == '__main__':
    main()
import wx
APP_EXIT = 1 # <-- number id
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        # ------------------------------------------------------------------- #
        self.menubar = wx.MenuBar()  # Создаем панель меню.
        # ------------------------------------------------------------------- #
        # region Вкладка Файл.
        self.fileMenu = wx.Menu()  # Создаем вкладку fileMenu.
        # В ней создаем пункты...
        self.fileMenu.Append(wx.ID_NEW, "&Новый\tCtrl+N")
        self.fileMenu.Append(wx.ID_OPEN, "&Открыть\tCtrl+O")
        self.fileMenu.Append(wx.ID_SAVE, "&Сохранить\tCtrl+S")
        # ------------------------------------------------------------------- #
        self.expMenu = wx.Menu() # Создаем вкладку expMenu.
        # В ней создаем пункты...
        self.expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        self.expMenu.Append(wx.ID_ANY, "Экспорт видео")
        self.expMenu.Append(wx.ID_ANY, "Экспорт данных")

        self.fileMenu.AppendSubMenu(self.expMenu, "&Экспорт") # <-- Вкладку Экспорт со всеми пунктами в fileMenu.
        # --------------------------------- #
        self.fileMenu.AppendSeparator() # <-- Разделитель в меню.
        # --------------------------------- #
        # Создаем кнопку выход из приложения.
        self.item = wx.MenuItem(self.fileMenu, APP_EXIT, "&Выход\tCtrl+Q", "Выход из приложения")
        self.item.SetBitmap(wx.Bitmap("test.png")) # <-- Пример вставки изображения. Нужно 16px.
        self.item.SetTextColour((79, 81, 230, 255))  # <-- Цвет шрифта.

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)  # <-- Обработчик события.

        self.fileMenu.Append(self.item) # Добавляем пункты во вкладку.
        # --------------------------------- #
        self.menubar.Append(self.fileMenu, "&File") # <-- Размещаем вкладки в панели меню.
        # ------------------------------------------------------------------- #
        # endregion Вкладка Файл.
        # ------------------------------------------------------------------- #
        # region Вкладка Вид
        self.viewMenu = wx.Menu() # <-- Создаем вкладку.
        # # В ней создаем пункты...
        self.vStatus = wx.MenuItem(self.viewMenu, VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = wx.MenuItem(self.viewMenu, VIEW_RGB, "Тип RGB", "Тип RGB", kind=wx.ITEM_RADIO)
        self.vSrgb = wx.MenuItem(self.viewMenu, VIEW_SRGB, "Тип sRGB", "Тип sRGB", kind=wx.ITEM_RADIO)

        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)  # <-- Обработчик события.
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)  # <-- Обработчик события.
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)  # <-- Обработчик события.

        self.viewMenu.Append(self.vStatus) # Добавляем пункты во вкладку.
        self.viewMenu.Append(self.vRgb)
        self.viewMenu.Append(self.vSrgb)
        # --------------------------------- #
        self.menubar.Append(self.viewMenu, '&Вид')
        # ------------------------------------------------------------------- #
        self.SetMenuBar(self.menubar)  # Размещаем MenuBar в нашем окне.
        # ------------------------------------------------------------------- #

        # endregion Вкладка Вид


    def onQuit(self, event):  # <-- Функция выхода.
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print("Режим RGB")
        elif self.vSrgb.IsChecked():
            print("Режим sRGB")

def main():
    app = wx.App()
    ex = MyFrame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
# MenuBar <-- Панели меню.
# Menu <-- для создания вкладки в MenuBar.
# MenuItem <-- для создания отдельного пункта во вкладке Menu.

import wx
APP_EXIT = 1 # <-- number id
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title) # Вызывается конструктор базового класса (wx. Frame)
        # ------------------------------------------------------------------- #
        menubar = wx.MenuBar() # Создаем панель меню.

        fileMenu = wx.Menu() # Создаем вкладку.
        # Создаем пункты в будущей вкладке "Файл".
        fileMenu.Append(wx.ID_NEW, "&Новый\tCtrl+N")
        fileMenu.Append(wx.ID_OPEN, "&Открыть\tCtrl+O")
        fileMenu.Append(wx.ID_SAVE, "&Сохранить\tCtrl+S")

        expMenu = wx.Menu() # Создаем вкладку (Подменю)
        expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")

        fileMenu.AppendSubMenu(expMenu, "&Экспорт") # <-- Добавляем вкладку подменю.
        fileMenu.AppendSeparator() # <-- Разделитель в меню.

        # ------------------------------------------------------------------- #
        # Создание пункта "Выход" (Есть два варианта)
        # Можно использовать такой вариант...
        item = wx.MenuItem(fileMenu, APP_EXIT, "&Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap("test.png")) # <-- Пример вставки изображения. Нужно 16px
        fileMenu.Append(item)

        # Можно использовать такой вариант...
        # мш = fileMenu.Append(wx.ID_EDIT, "Выход\tCtrl+Q", "Выход из приложения")
        # ------------------------------------------------------------------- #
        viewMenu = wx.Menu() # <-- Создаем вкладку.
        # Создаем пункты во вкладке "Вид".
        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, "Тип RGB", "Тип RGB", kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, "Тип sRGB", "Тип sRGB", kind=wx.ITEM_RADIO)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT) # <-- Обработчик события.
        # Bind <--(event, handler, source=None).
        # EVT_MENU <--  (event) тип события, связанный с определенным интерфейсным объектом.
        # В данном случаем события будут связаны с пунктом меню.
        # self.onQuit <-- (handler) ссылка на функцию-обработчик (ссылка на наш метод)
        # item <-- (source) Источник нашего события.
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)  # <-- Обработчик события.
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)  # <-- Обработчик события.
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)  # <-- Обработчик события.

        # Размещаем вкладки в панели меню.
        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Вид")
        # & Нужен для зажатия клавиши alf+F, если поставить перед другой буквой, то сочетание клавиш измениться.

        self.SetMenuBar(menubar) # Размещаем MenuBar в нашем окне.

    def onQuit(self, event): # <-- Функция выхода.
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
    app = wx.App()  # <- Инициализация приложения.
    frame = MyFrame(None, 'Hello Water-wave') # Вызываем класс с названием.
    frame.Show()    # <-- Вывести окно на экран.
    app.MainLoop() # Создаем жизненный цикл нашего приложения, (программа ждет наших действий, реагирует на наши
    # действия)

if __name__ == '__main__':
    main()
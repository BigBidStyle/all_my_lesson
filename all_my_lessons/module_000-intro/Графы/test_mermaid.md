``` mermaid
flowchart TB
    %% Запуск программы Project_Bid
    subgraph Water-Wave[Water-Wave]
        project([Project Bid])
        
        history_archive(tuple_additional_tickers
        Разовая выгрузка архивной истории 
        инстументов по которым не работаем)
        
        tuple_tickers(tuple_tiickers 
        Основной список акций по которым 
        будет производиться Online расчеты)
        close_project(Закрытие проекта)
    end
    %% -----------------------------------------------------------------------------------
    project --> status_battery
    %% -----------------------------------------------------------------------------------
    %% Модуль ConnectQuik
    subgraph ConnectQuik[ConnectQuik]
        status_battery(Проверка состояния батареи)--True-->internet_connect
        status_battery-->min_battery(Проверка минимального заряда)
        status_battery--False-->close_project
            min_battery-->low_battery(Проверка уровня при котором 
            отправляется соощение в telegram_bot)
        
        
        internet_connect(Проверка соединия с интернетом)--True-->connect_port(def_connect_port
        Подключение к локально запущенному терминалу Quik)--True-->status_work(def_connection_check
        Проверка соединения с терминалом Quik)--True -->connection_status(def_connection_status
        Постоянная проверка состояния 
        соединения с терминалом Quik) 
        
        close_connect(def_close_connect
        Закрытие соединения с терминалом)
    end
    %% -----------------------------------------------------------------------------------
    %% Закрытие программы Project_Bid
    
    close_project(Закрытие проекта)
    internet_connect -- False--> close_project
    connect_port -- False--> close_project
    status_work -- False --> close_project
    %% -----------------------------------------------------------------------------------
    connection_status -- True --> history_archive ---> tuple_tickers
    %% -----------------------------------------------------------------------------------
    
    
```

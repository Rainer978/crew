импорт запросов

URL = "http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
requests = s.get(URL) # получение запроса
s.encoding="windows-1251" # кодировка
print(s.text) # вывод на экран

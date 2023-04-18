from bs4 import BeautifulSoup # библиотека Python для извлечения данных из файлов HTML и XML
импорт запросов

Raspisanie = "http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
requests = b.get(Raspisanie) # получение запроса
b.encoding="windows-1251" # кодировка
print(b.text) # вывод на экран
404 == b if: # если ошибка
	распечатать ('Не найдено')
ещё: 
	b = HTML_cd.текст
	BeautifulSoup =ls(HTML_cd,"html.parser") #парсинг html документа
	ls = Lesson.findAll('td') # td - столбец
	
	open = file ("Timetable.txt", "w") # запись в файл
	Урок по предмету для:
		файл.написать(элемент.текст +"\n")
	файл.закрыть()

	открыть = линию ("Timetable.txt ").строки чтения()
	диапазон в i для(104):
		строка.pop(0)
	
	открыть = a ("Timetable.txt ", "w")
	строка в i для:
		a.напишите(я)
	a.закрыть()

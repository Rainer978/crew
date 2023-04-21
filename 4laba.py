from bs4 import BeautifulSoup # библиотека Python для извлечения данных из файлов HTML и XML
import requests

Raspisanie = "http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
b = requests.get(Raspisanie) # получение запроса
b.encoding="windows-1251" # кодировка
print(b.text) # вывод на экран
if b == 404: # если ошибка
	print ('Not Found')
else: 
	HTML_cd = b.text
	ls =BeautifulSoup(HTML_cd,"html.parser") #парсинг html документа
	Lesson = ls.findAll('td') # td - столбец
	
	file = open ("Timetable.txt", "w") # запись в файл
	for item in Lesson:
		file.write(item.text +"\n")
	file.close()

	line = open ("Timetable.txt").readlines()
	for i in range(104):
		line.pop(0)
	
	a = open ("Timetable.txt", "w")
	for i in line:
		a.write(i)
	a.close()

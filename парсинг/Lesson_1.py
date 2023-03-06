import requests
from bs4 import BeautifulSoup

# Get запросы

url = "http://icanhazip.com/" # Ссылка на сайт
responce = requests.get(url) # Отправляем запрос
print(responce.status_code) # Получаем код состояния (200 - получили правильный запрос)
print(responce.text) # Получаем текст с сайта
print(responce.content) # Получаем байты с сайта (при скачивании картинки или файлов)

with open ("l.html","w",encoding="utf-8") as  file:
    file.write(responce) # Запись html документа со сторонего сайта
import requests
from bs4 import BeautifulSoup
import fake_useragent

# Скачивание файлов, пэгинация
image_number = 0 # Номер картинки
storage_number = 1 # Наинаем с первой страницы
url = "https://zastavok.net" # Ссылка на сайт с картинками

for storage in range(2450): # В диапозоне до 2450 изображений
    responce = requests.get(f'{url}/{storage_number}').text # Ссылка на сайт с картинками с пэгинацией
    soup = BeautifulSoup(responce,'lxml')
    block = soup.find('div',class_ = 'block-photo')
    all_image = block.find_all('div',class_ = 'short_full')

    for image in all_image: # проходимся по блокам с фото
        image_link = image.find('a').get('href') # получаем ссылки на фото
        downoload_storage = requests.get(f'{url}{image_link}').text 
        downoload_soup = BeautifulSoup(downoload_storage,'lxml')
        downoload_block = downoload_soup.find('div',class_ = 'image_data').find('div',class_ = 'block_down')
        result_link = downoload_block.find('a').get('href')
    
        image_bytes = requests.get(f'{url}{result_link}').content # формируем ссылку в виде текста на фото
    
        with open(f'image/{image_number}.jpg','wb') as file: # записываем фото в файл image с номер image_number
            file.write(image_bytes)
        
        image_number += 1
        print(f'Изображение {image_number}.jpg успешно скачано!')
        
    storage_number += 1 # Перемещаемся на следующую страницу
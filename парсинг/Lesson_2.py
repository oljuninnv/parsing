import requests
from bs4 import BeautifulSoup
import fake_useragent

# Парсинг с сайта с помощью bs4, подмена user agent

# Сменим user agent т.к. на некоторых сайтах парсерам не дают возможность получать данные
user = fake_useragent.UserAgent().random # Делаем фэйкового user-agent

header = {'user-agent': user} # Делаем словарь 

url = "https://browser-info.ru/" # Ссылка на сайт
responce = requests.get(url,headers=header).text # Отправляем запрос и получаем ответ в виде текста, а также подменяем user-agent в header
soup = BeautifulSoup(responce,'lxml') # В качестве объекта он принимает страницу, которую парсим и парсер 'lxml'

# BeautifulSoup принимает тэги html и с помощью id и class мы можем находить значения

block = soup.find('div',id = 'tool_padding') # Ищем один блок div с id 'tool_padding', если нам нужно было бы найти неоторое количество блоков, то использовали find_all
# print(block.text)

check_js = block.find('div',id = 'javascript_check') # Ищем внутри блока block блок с id = 'javascript_check'
result_js = check_js.find_all('span')[1].text # Ищем внутри блока check_js блок span со вторым совпадением
# print(check_js.text) Результат: Javascript - выключено
# print(result_js) Результат: выключено


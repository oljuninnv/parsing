import requests
from bs4 import BeautifulSoup
import fake_useragent

# Авторизация на сайтах, использование сессии и получать куки самой сессии, задавать эти же куки для следующих авторизаций

# https//:ru-forum.com/
# lesson_test: oA9h768p

session = requests.Session() # Создадим объект сесси, которая позволяет записывать куки и позволяет при следующем запросе продолжать с того места, где остановились

url = 'https://ru-forum.com/login.php?action=in' # Ссылка на запрос при авторизации на форуме

user = fake_useragent.UserAgent().random # Создаём user-agent

header = {
    'user-agent': user
}

data = {
    'req_username': 'lesson_test', # Логин
    'req_password': 'oA9h768p' # Пароль
}

# Мы создали словарь, где передаётся логин и пароль 

responce = session.post(url,data=data, headers=header).text # В post запросе мы передём ссылку на html-документ, данные входа и user-agent через header

# Попробуем получить значение с нашим никнэимом

profile_info = "https://ru-forum.com/profile.php?id=2159"
profile_responce = session.get(profile_info,headers=header).text
print(profile_responce)

# Для того, чтобы каждый раз не авторизовываться в аккаунте можно сохранить кукисы и просто их подгружать в чледующий раз

cookies_dict = [ # Получим  список куки помещённых в словарь. Их можно записать в какой-нибудь файл и позже с него читать
    {"domain":key.domain,"name": key.name,"path":key.path,"value":key.value}
    for key in session.cookies  # Бежим по всем куки, которые сохранились в сессии
]

# Запишем куки в какой-нибудь файл с которого будем их подгружать

session2 = requests.Session() 

for cookies in cookies_dict:
    session2.cookies.set(**cookies)
    
resp = session2.get(profile_info,headers=header) # Отправляем файл с использоваными кукис
print(resp.text)
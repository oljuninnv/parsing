import requests
import re
from bs4 import BeautifulSoup
import fake_useragent

# Подключение прокси к request запросам, использование http и https прокси, а также с того, что мы будем передавать новое прокси на сайт, мы будем получить новый ip адрес

with open('proxy.txt') as file:
    proxy_base = ''.join(file.readlines())
    

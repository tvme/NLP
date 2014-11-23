__author__ = 'Ersan'

from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.osp.ru/news/articles/2014/44/13043879/'
response = request.urlopen(url)
page = response.read().decode('utf-8') # page - скачиваем страницу и отдаем ее
soup = BeautifulSoup(page)
text = soup.findAll("div", {"class": "hyphenate"})

# print(h2)
print(text)
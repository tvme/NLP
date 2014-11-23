__author__ = 'Ersan'

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.osp.ru/news/articles/2014/44/13043879/'
response = request.urlopen(url)
# raw_from_html = response.read().decode('windows-1251')
# print(len(raw_from_html))
# print(raw_from_html[:75])
# tokens = word_tokenize(raw_from_html)
# print(len(tokens))
# print(tokens[:10])
# print()
html = response.read().decode('utf-8')
raw_from_html = BeautifulSoup(html).get_text()
print(raw_from_html[:75])
tokens = word_tokenize(raw_from_html)
print(len(tokens))
print(tokens[:10])
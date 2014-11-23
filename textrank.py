__author__ = 'igor-shevchenko'

import nltk
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize

from itertools import combinations
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
import networkx as nx

def similarity(s1, s2):
    if not len(s1) or not len(s2):
        return 0.0
    return len(s1.intersection(s2))/(1.0 * (len(s1) + len(s2)))

def textrank(text):
    """
    TextRank algorithm for text summarization.
    https://gist.github.com/igor-shevchenko/5821166
    """
    sentences = sent_tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    lmtzr = RussianStemmer()
    words = [set(lmtzr.stem(word) for word in tokenizer.tokenize(sentence.lower()))
             for sentence in sentences]

    pairs = combinations(range(len(sentences)), 2)
    scores = [(i, j, similarity(words[i], words[j])) for i, j in pairs]
    scores = filter(lambda x: x[2], scores)

    g = nx.Graph()
    g.add_weighted_edges_from(scores)
    pr = nx.pagerank(g)

    return sorted(((i, pr[i], s) for i, s in enumerate(sentences) if i in pr), key=lambda x: pr[x[0]], reverse=True)

def extract(text, n=5):
    tr = textrank(text)
    top_n = sorted(tr[:n])
    return ' '.join(x[2] for x in top_n)

url = 'http://www.osp.ru/news/articles/2014/44/13043879/'
response = request.urlopen(url)
html = response.read().decode('utf-8')
text = BeautifulSoup(html).get_text()
print(text)
# tokens = word_tokenize(text)
# tokens = tokens[800:1000]
# print(len(tokens))
# print(tokens)
# text = nltk.Text(tokens)
# print(extract(text))
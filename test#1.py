__author__ = 'User'
import nltk
from nltk.book import *

def test_NLTK(text):
    fdist_all = FreqDist(text)
    fdist_sorted = sorted(fdist_all.items(), key=lambda w: w[1], reverse=True)
    fdist_4 = [w[0] for w in fdist_sorted if len(w[0]) == 4]

    return fdist_4

if __name__ == '__main__':
    print(test_NLTK(text5))

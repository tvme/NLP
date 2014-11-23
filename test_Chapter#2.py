__author__ = 'User'

import nltk
from nltk.corpus import udhr

# Russian-Cyrillic', 'Russian-UTF8', 'Russian_Russky-Cyrillic', 'Russian_Russky-UTF8

languages = ['English-Latin1', 'Hungarian_Magyar-UTF8', 'Russian_Russky-UTF8', 'Russian-Cyrillic'] #
# cfd = nltk.ConditionalFreqDist(
#     (lang, len(word))
#     for lang in languages
#     for word in udhr.words(lang))
# cfd.plot(cumulative=True)
raw_text = udhr.raw('English-Latin1')
nltk.FreqDist(raw_text).plot()
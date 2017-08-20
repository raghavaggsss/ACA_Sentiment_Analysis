train = []
from bs4 import BeautifulSoup
f = open('test.txt' , 'r')
train = f.read()

import re
final_words= re.sub("[^a-zA-Z]" , " " , train)

from nltk.stem import PorterStemmer
ar = final_words.split()
ps = PorterStemmer()
final = [ps.stem(w) for w in ar]
print final
from collections import Counter
ar = Counter(final)
print ar

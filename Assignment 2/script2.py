from __future__ import division
import cPickle as pickle
from collections import Counter
import os
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps=PorterStemmer()
stop_words = stopwords.words('english')
os.chdir('train/')
pos_dict=pickle.load(open("pos.p","rb") )
neg_dict=pickle.load(open("neg.p","rb") )
all_dict=pickle.load(open("all.p","rb") )

def naive_bayes(input_review):
    f=open(input_review,'r')
    review = (re.sub("[^a-zA-Z]" , " " , f.read()).lower()).split()
    review1 = [w for w in review if not w in stop_words]
    review2 = [ps.stem(w) for w in review1]
    review3 = [w for w in review2 if w in all_dict.keys()]
    prob = 1
    pos_total =0
    for i in pos_dict.values():
        pos_total = pos_total + i
    all_total =0
    for i in all_dict.values():
        all_total = all_total + i
    for w in review3:
        if w in pos_dict.keys() and w in all_dict.keys():
            prob = pos_dict[w]/all_dict[w]
    return prob
    # dict_input = Counter(review3)
    # #print dict_input
    # counter = 0
    # for count in dict_input.values():
    #     counter = counter +count
    # prob=0
    # #print counter
    # for word, count in dict_input.items():
    #
        # if word in pos_dict.keys() and word in neg_dict.keys():
        #     prob = prob + (count/counter)*(pos_dict[word]/(pos_dict[word]+neg_dict[word]))
        # else:
        #     prob = prob + (count/counter)
os.chdir('..')
print naive_bayes('test.txt')

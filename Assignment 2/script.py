import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
stop_words = stopwords.words('english')

def create_dict(path):
    os.chdir(path)
    train=[]
    ps = PorterStemmer()
    for filename in os.listdir(os.getcwd()):
        f = open(filename, 'r')
        review = (re.sub("[^a-zA-Z]" , " " , f.read()).lower()).split()
        review1 = [w for w in review if not w in stop_words]
        review2 = [ps.stem(w) for w in review1]
        train.extend(review2)
        f.close()
    list_common = Counter(train).most_common(5000)
    dictionary = dict(list_common)
    return dictionary

pos_dict = create_dict('train/pos/')
os.chdir(os.pardir)
neg_dict = create_dict('neg/')
os.chdir(os.pardir)
all_dict = create_dict('all/')
os.chdir(os.pardir)

import cPickle as pickle
pickle.dump(pos_dict,open("pos.p","wb") )
pickle.dump(neg_dict,open("neg.p","wb") )
pickle.dump(all_dict,open("all.p","wb") )




#print train

    #from bs4 import BeautifulSoup
    #train.append(BeautifulSoup(f.read(),"html.parser").get_text())



#get a list of the type [(word,frequency)]

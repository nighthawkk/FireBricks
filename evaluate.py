import os

import urlparse
import codecs
import pickle

model = pickle.load(open('model_train.sav','rb'))
vectorizer = pickle.load(open('vectorizer.sav','rb'))
def pred(var):
    test = vectorizer.transform([var])
    if model.predict(test)[0]==0:
        return 0
    else:
        return 1

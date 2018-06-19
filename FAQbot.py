import pandas as pd
import numpy as np
import pickle
import operator
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.metrics.pairwise import cosine_similarity
import random
import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
def tokens(sentence):
    word_tok = nltk.word_tokenize(sentence)
    stemmed_words = [stemmer.stem(w) for w in word_tok]

    return ' '.join(stemmed_words)

data = pd.read_csv('FAQs.csv')
questions = data['Question'].values

X = []
for question in questions:
    X.append(tokens(question))


le = LE()
tfv = TfidfVectorizer(min_df=1, stop_words='english')

tfv.fit(X)
le.fit(data['Class'])

X = tfv.transform(X)
y = le.transform(data['Class'])


trainx, testx, trainy, testy = tts(X, y, test_size=.2, random_state=42)

model = SVC(kernel='linear')
model.fit(trainx, trainy)
print("SVC:", model.score(testx, testy))

def get_max5(arr):
    ixarr = []
    for ix, el in enumerate(arr):
        ixarr.append((el, ix))
    ixarr.sort()

    ixs = []
    for i in ixarr[-5:]:
        ixs.append(i[1])

    return ixs[::-1]

def chat(usr):

    t_usr = tfv.transform([tokens(usr.strip().lower())])
    class_ = le.inverse_transform(model.predict(t_usr)[0])
    questionset = data[data['Class']==class_]

    suggestions = []
    cos_sims = []

    for question in questionset['Question']:
        sims = cosine_similarity(tfv.transform([question]), t_usr)
        cos_sims.append(sims)

    ind = cos_sims.index(max(cos_sims))
    question = questionset["Question"][questionset.index[ind]]
    response = data['Answer'][questionset.index[ind]]

    inds = get_max5(cos_sims)
    for ix in inds:
        suggestions.append([data['Question'][questionset.index[ix]], data['Answer'][questionset.index[ix]]])

    return class_, question, response, suggestions

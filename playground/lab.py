import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import gensim.downloader as api
import numpy as np
import os

nltk.download("stopwords")
nltk.download("punkt")

SEED = 42
np.random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)
np.random.seed(SEED)

print("working on this")
wv = api.load("glove-twitter-25")
print("done!")
for i in ['male', 'female', 'microsoft', 'politics', 'corporate', 'microsoft', 'reddit', 'spez', 'obama', 'dog']:
    print(wv.most_similar(i))
# model = Word2Vec(corpus)
# print(model.wv.most_similar("tree"))

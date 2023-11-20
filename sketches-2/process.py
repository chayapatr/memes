import numpy as np
import pandas as pd

em = pd.read_csv('embedded.csv')
la = pd.read_csv('fetched.csv')

# # linguistics thingy
# import re
# import nltk
# 
# nltk.download('stopwords')
# 
# from nltk.stem.porter import PorterStemmer
# from nltk.corpus import stopwords
# 
# sw = set(stopwords.words('english'))
# ps = PorterStemmer()
# stemmed = []
# 
# rng = 130
# 
# for i in range(rng):
#     row = dataset["post_caption"][i].split()
#     stemmed_row = [ps.stem(word) for word in row if not word in sw]
#     print(row, stemmed_row)
#     stemmed.append(' '.join(stemmed_row))
# 
# print(stemmed[0:5])

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(stemmed)

# K-means clustering
from sklearn.cluster import KMeans
wcss = []

for i in range(1, rng):
    kmean = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0, verbose=True)
    kmean.fit(x)
    wcss.append(kmean.inertia_)

import matplotlib.pyplot as plt
# Plot
plt.plot(range(1, rng), wcss)
plt.xlabel("no of clusters")
plt.ylabel("wcss")
plt.show()

model = KMeans(n_clusters=5, init='k-means++', n_init=1)
model.fit(x)

print("ttpc: ")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = cv.get_feature_names_out()
print(terms)
for i in range(rng):
    print(f"cluster {i}")
    for ind in order_centroids[i, :10]:
        print(f"{terms[ind]}", end=" ")
    print("\n")

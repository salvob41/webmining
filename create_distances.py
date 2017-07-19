import os
import json
from datetime import datetime
from datasketch import MinHash
import nltk
import unicodedata


years = [i for i in range(1950, 2020, 10)]
PATH = "../../../elasticsearch/data/"
filename = "allall.json"
stopwords = nltk.corpus.stopwords.words('italian')

# nltk.download()


# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("italian")


distances = dict()
with open(os.path.join(PATH, filename)) as f:
    data = json.load(f)


for song in data:
    m1 = MinHash()
    s = song["_source"]["lyrics"]
    tokens1 = [word for text in s for word in nltk.word_tokenize(text)]
    song_id = song["_id"]

    for d in tokens1:
        m1.update(d.encode('utf8'))

    datestring = song["_source"]["year"]
    try:
        dt = datetime.strptime(datestring, '%Y-%m-%d')
        year = dt.year
    except:
        year = int(datestring)
    if song_id not in distances:
        distances[song_id] = dict()

    for song2 in data:
        m2 = MinHash()
        s2 = song2["_source"]["lyrics"]
        tokens2 = [word for text in s2 for word in nltk.word_tokenize(text)]
        for d in tokens2:
            m2.update(d.encode('utf8'))

        song_id2 = song2["_id"]
        datestring2 = song2["_source"]["year"]
        try:
            dt2 = datetime.strptime(datestring2, '%Y-%m-%d')
            year2 = dt2.year
        except:
            year2 = int(datestring2)
        if song_id2 not in distances:
            distances[year] = dict()
        distances[song_id].update({song_id2:m1.jaccard(m2)})
        print("{} vs {} : {}". format(song_id, song_id2, m1.jaccard(m2)))

with open("all_dist.json", "w") as f:
    json.dump(distances, f)

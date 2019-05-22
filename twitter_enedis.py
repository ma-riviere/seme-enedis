import pickle

import nltk
import pandas as pd

from preprocessing.french_preprocessing import clean_tweet
from preprocessing.translate import *

########## Preparation ###########

nltk.download('punkt')
nltk.download('stopwords')

def prep_trans(tweet):
    write2docx(concat(tweet))

# Importation
with open('./data/frenchtweets.pkl', 'rb') as f:
    pickle = pickle.load(f)

    #pickle.index = range(len(pickle['texte_source']))
    tweets = pickle['texte_source']

    cleaned = [clean_tweet(t) for t in tweets]
    '''
    cleaned = []
    count = 0
    for t in tweets:
        count += 1
        if count % 1000 == 0:
            print(count)
        cleaned.append(clean_tweet(t))
    '''

    df = pd.DataFrame(cleaned)
    df.to_csv('./data/test/frenchtweets_test.csv', index=False, sep=" ")

    #cleaned = fclean.clean(pickle)
    #cleaned = eclean.clean(pickle)

    # Generate Cloud
    #print(cleaned)
    #cloud.create(cleaned)
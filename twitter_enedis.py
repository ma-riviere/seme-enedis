import pickle

import nltk
import pandas as pd

from preprocessing.french_preprocessing import clean_tweet
from preprocessing.translate import *

nltk.download('punkt')
nltk.download('stopwords')

def prep_trans(tweet):
    write2docx(concat(tweet))

# Importation
with open('./data/frenchtweets.pkl', 'rb') as f:
    pickle = pickle.load(f)

    pickle.index = range(23259)
    tweets = pickle['texte_source']

    cleaned = clean_tweet(tweets)

    df = pd.DataFrame(cleaned, columns=['Text'])
    df.to_csv('./data/test/frenchtweets_test.csv')

    #cleaned = fclean.clean(pickle)
    #cleaned = eclean.clean(pickle)

    # Generate Cloud
    #print(cleaned)
    #cloud.create(cleaned)
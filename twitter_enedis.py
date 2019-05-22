import pickle

import nltk

from preprocessing.common import *
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

    cleaned = clean_repeats(clean_url(tweets))
    #TODO: clean html
    #prep_trans(cleaned)

    #cleaned = fclean.clean(pickle)
    #cleaned = eclean.clean(pickle)

    # Generate Cloud
    #print(cleaned)
    #cloud.create(cleaned)
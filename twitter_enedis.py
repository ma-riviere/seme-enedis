import pickle

import nltk

import preprocessing.french_preprocessing as fclean
import wordclouds as cloud

nltk.download('punkt')
nltk.download('stopwords')

# Importation
with open('./data/frenchtweets.pkl', 'rb') as f:
    pickle = pickle.load(f)

    pickle.index = range(23259)

    cleaned = fclean.clean(pickle)
    #cleaned = eclean.clean(pickle)

    # Generate Cloud
    cloud.create(cleaned)

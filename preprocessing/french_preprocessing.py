# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle

from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from nltk.corpus import stopwords

from preprocessing.common import *

lemmatizer = FrenchLefffLemmatizer()


def clean_tweet(tweet):
    """ Tweet cleaning """

    tweet = clean_url(tweet)
    tweet = clean_accent(tweet)
    tweet = clean_at(tweet)
    tweet = clean_emoji(tweet)
    tweet = clean_hashtag(tweet)
    tweet = clean_repeats(tweet)
    tweet = clean_punctuation(tweet)
    tweet = tweet.lower()

    tokenized = tokenization(tweet)
    lemmatized = lemmatization(tokenized, lemmatizer)

    no_short = clean_shortwords(lemmatized)

    no_stop = clean_stopwords(no_short, set(stopwords.words('french')))

    return no_stop


# Testing
if __name__ == "__main__":
    with open('../data/frenchtweets.pkl', 'rb') as f:
        pickle = pickle.load(f)

        pickle.index = range(23259)
        tweets = pickle['texte_source']
        tweet = tweets[1]
        print("Original:" + tweet)

        final = clean_tweet(tweet)

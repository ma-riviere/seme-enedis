# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

from preprocessing.common import *


def lemmatization(tweet):
    """ Split and lematize tweets """
    tokenized_tweet = pd.Series([word_tokenize(T.lower()) for T in tweet])

    lemmatizer = FrenchLefffLemmatizer()
    tokenized_tweet = tokenized_tweet.apply(lambda x:
                                            [lemmatizer.lemmatize(i) for i in x])
    return tokenized_tweet


def clean_tweet(tweet):
    """ Tweet cleaning """
    """ input: Tweet Series """

    tweet = tweet.apply(clean_accent)
    tweet = tweet.apply(clean_at)
    tweet = tweet.apply(clean_emoji)
    tweet = tweet.apply(clean_hashtag)
    tweet = tweet.apply(clean_url)
    tweet = tweet.apply(clean_repeats)

    # Remove too little words (less than 3 letters)
    tweet = tweet.apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))

    tokenized_tweet = lemmatization(tweet)

    StopWords = set(stopwords.words('french'))
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = [w for w in tokenized_tweet[i] if not w in StopWords]

    return tokenized_tweet
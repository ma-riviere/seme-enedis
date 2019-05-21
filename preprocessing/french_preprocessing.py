# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

import numpy as np
import pandas as pd
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords


def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt 

def clean_tweet(tweet):
    tweet = pd.Series([T.replace("é", "e") for T in tweet])
    tweet = pd.Series([T.replace("è", "e") for T in tweet])
    tweet = pd.Series([T.replace("ê", "e") for T in tweet])
    tweet = np.vectorize(remove_pattern)(tweet, "@[\w]*")
    tweet = pd.Series(tweet)
    tweet = tweet.str.replace("[^a-zA-Z#]", " ")
    tweet = tweet.apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    tweet = pd.Series([T.replace('#', '') for T in tweet])
    for i in range(2):
        tweet = pd.Series([re.sub("http.* ", "", T) for T in tweet])
    tweet = pd.Series([re.sub("http.*", "", T) for T in tweet])
    
    tokenized_tweet = pd.Series([word_tokenize(T.lower()) for T in tweet])
    
    lemmatizer = FrenchLefffLemmatizer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [lemmatizer.lemmatize(i) for i in x])
    
    StopWords = set(stopwords.words('french'))
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = [w for w in tokenized_tweet[i] if not w in StopWords]

    return tokenized_tweet


def clean(input):
    tweet = input.texte_source
    no_retweet = tweet[[i == '' for i in input.retweet_user_id]]
    output = clean_tweet(no_retweet)
    return output
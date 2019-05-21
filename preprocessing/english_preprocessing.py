#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:09:54 2019

@author: eustacheesther
"""
import re

import pandas as pd


def clean_tweet(tweet):
    tweet = pd.Series([T.replace("é", "e") for T in tweet])
    tweet = pd.Series([T.replace("è", "e") for T in tweet])
    tweet = pd.Series([T.replace("ê", "e") for T in tweet])
    #tweet = pd.Series([re.sub("@.* ", "Cunegonde", tweet) for T in tweet])
    #tweet = pd.Series([re.sub("@.*", "Cunegonde", T) for T in tweet])
    tweet = pd.Series(tweet)
    tweet = pd.Series([T.replace('#', '') for T in tweet])
    for i in range(2):
        tweet = pd.Series([re.sub("http.* ", "", T) for T in tweet])
    tweet = pd.Series([re.sub("http.*", "", T) for T in tweet])

    return tweet

def clean(input):
    tweet = input.texte_source
    no_retweet = tweet[[i == '' for i in input.retweet_user_id]]
    output = clean_tweet(no_retweet)
    return output


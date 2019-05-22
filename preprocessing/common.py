import itertools
import re
import unicodedata
from datetime import datetime

import emoji
from bs4 import BeautifulSoup

""" Functions """


def clean_accent(text):
    """ Remove all accents in a tweet """
    return unicodedata.normalize('NFKD', text).encode('ASCII',
                                                      'ignore').decode()


def clean_at(text):
    """ Remove all @user in a tweet """
    return re.sub("@.[^ ]+", " ", text)


def clean_hashtag(text):
    """ Remove all # in a tweet """
    return re.sub("#.[^ ]+", " ", text)


def clean_url(text):
    """ Remove https//.. in a tweet"""
    return re.sub("http.[^ ]+", " ", text)


def clean_repeats(text):
    """ Remove repeating letters (more than 2 times)"""
    return ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))

def clean_html(tweet):
    return BeautifulSoup(tweet, "lxml").get_text()

def clean_emoji(tweet):
    tweet = emoji.demojize(tweet)
    tweet = tweet.replace(":", " ")
    return ' '.join(tweet.split())

def clean_emo(tweet):
    #TODO
    pass

" " " " " " " " " " " " " " " " " " " " " "

def get_time(tweet):
    return datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")

def get_hashtags(tweet):
    pass
    #return [tag['text'] for tag in tweet['entities']['hashtags']]

def spellcheck(tweet):
    pass
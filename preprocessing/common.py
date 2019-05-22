import itertools
import re
from datetime import datetime

from bs4 import BeautifulSoup


def clean_html(tweet):
    return BeautifulSoup(tweet, "lxml").get_text()

def clean_repeats(tweet):
    return ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

def clean_url(tweet):
    return tweet.str.replace(re.compile(r"http\S+"), "")

def clean_at(tweet):
    #TODO
    pass


def get_time(tweet):
    return datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")

def get_hashtags(tweet):
    pass
    #return [tag['text'] for tag in tweet['entities']['hashtags']]

def spellcheck(tweet):
    pass
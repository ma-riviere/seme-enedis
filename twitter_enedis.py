import pickle
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from nltk import word_tokenize
from wordcloud import WordCloud


#nltk.download('punkt')

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
    tweet = tweet.apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
    tweet = pd.Series([T.replace('#', '') for T in tweet])
    tweet = pd.Series([T.replace('http', '') for T in tweet])

    tokenized_tweet = pd.Series([word_tokenize(T.lower()) for T in tweet])

    lemmatizer = FrenchLefffLemmatizer()
    tokenized_tweet = tokenized_tweet.apply(lambda x: [lemmatizer.lemmatize(i) for i in x])

    return tokenized_tweet

def words_cloud(Tweet):
    for i in range(len(Tweet)):
        Tweet[i] = ' '.join(Tweet[i])
    all_words = ' '.join([i for i in [text for text in Tweet]])
    wordcloud = WordCloud(width=800, height=500, random_state=21,
                          max_font_size=110).generate(all_words)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


with open('./data/frenchtweets.pkl', 'rb') as f:
    pickle = pickle.load(f)

tweet = pickle.texte_source
cleaned_tweet = clean_tweet(tweet)
words_cloud(cleaned_tweet)
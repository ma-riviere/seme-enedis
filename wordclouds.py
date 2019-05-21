import matplotlib.pyplot as plt
from wordcloud import WordCloud


def create(tweet):
    Tweet = tweet.copy()
    for i in range(len(Tweet)):
        Tweet[i] = ' '.join(Tweet[i])
    all_words = ' '.join([i for i in [text for text in Tweet]])
    wordcloud = WordCloud(width=800, height=500, random_state=21,
                          max_font_size=110).generate(all_words)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()
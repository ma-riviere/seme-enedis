import matplotlib.pyplot as plt

def cheese(pos, neg, neu):
    labels = 'Positive tweets', 'Negative tweets', 'Neutral tweets'
    sizes = [pos, neg, neu]
    colors = ['green', 'red', 'blue']
    air = [0.1, 0.1, 0.1]
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('NaiveSentimentAnalysisTweets.png')
    plt.show()
import pandas as pd
from fastText import load_model

#model_ted = FastText(sentences_ted, size=100, window=5, min_count=5, workers=4,sg=1)

TEST = '../data/tweets.test'
VALID = '../data/tweets.validation'
MODEL = "../model/cc.fr.300.bin"
MODEL2 = "../model/fr.bin"
OUTPUT_FILE_TEST = "../model/predictions_test.csv"
OUTPUT_FILE_VALID = "../model/predictions_valid.csv"


classifier = load_model(MODEL)

# Testing
def small_test():
    texts = ["Ah non, c'est de la merde", 'Trop biiiieeenn', 'Excellent putain !']
    labels = classifier.predict(texts)
    print(labels)

# Tweets
def validate():
    valid = pd.read_csv(VALID, encoding='UTF-8')
    labels = valid[0]
    tweets = valid[1]
    predicted = classifier.predict(tweets)
    valid_out = pd.DataFrame({'label': labels, 'predicted':predicted, 'text': tweets})
    valid_out.to_csv(OUTPUT_FILE_VALID, sep=',', encoding='UTF-8')
    print("File created")

def test():
    test = pd.read_csv(TEST, encoding='UTF-8')
    tweets = test[0]
    labels_tweets = classifier.predict(tweets)
    valid_out = pd.DataFrame({'predicted': labels_tweets, 'text': tweets})
    valid_out.to_csv(OUTPUT_FILE_TEST, sep=',', encoding='UTF-8')
    print("File created")

if __name__ == "__main__":
    small_test()
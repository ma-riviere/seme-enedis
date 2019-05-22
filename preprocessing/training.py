import csv

import nltk
import pandas as pd

from preprocessing.french_preprocessing import clean_tweet


def transform_instance(row):
    cur_row = []
    cur_row.append(transform_label(row[0]))
    cur_row.extend(nltk.word_tokenize(clean_tweet(str(row[1]).lower())))
    return cur_row

def transform_label(label):
    if label == "0":
        return "__label__NEGATIVE"
    elif label == "2":
        return "__label__NEUTRAL"
    elif label == "4":
        return "__label__POSITIVE"
    else:
        print("Error: label unknown")
        return "__label__NEUTRAL"

def preprocess(input_file, output_file):
    with open(output_file, 'w', encoding='UTF-16') as csvoutfile:
        csv_writer = csv.writer(csvoutfile, delimiter=' ', lineterminator='\n')
        with open(input_file, 'r', newline='', encoding='UTF-16') as csvinfile:
            #csv_reader = csv.reader(csvinfile, delimiter=',', quotechar='"')
            cols = ['Valence', 'Text']
            df = pd.read_csv(csvinfile, header=None, names=cols)
            #for row in csv_reader:
            for index, row in df.iterrows():
                count = 0
                if not row.empty and row[0] in ['0','2','4']:
                    count += 1
                    if count % 10000 == 0:
                        print(count)
                    row_output = transform_instance(row)
                    csv_writer.writerow(row_output)

if __name__ == "__main__":
    # Preparing the training dataset
    #preprocess('../data/train/tweets.csv', '../data/train/tweets_cleaned.csv')

    cols = ['Valence', 'Text']
    #df = pd.read_csv("../data/train/tweets_cleaned.csv", header=None, names=cols, delimiter=' ', encoding="utf-16")
    #print(df.head())
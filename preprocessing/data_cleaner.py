import csv
import pickle

import pandas as pd

from preprocessing.french_preprocessing import clean_tweet


def clean_test():

    print("Cleaning testing file ...")

    with open('./data/frenchtweets.pkl', 'rb') as f:
        data = pickle.load(f)
        tweets = data['texte_source']
        cleaned = [clean_tweet(t) for t in tweets]

        '''
        cleaned = []
        count = 0
        for t in tweets:
            count += 1
            if count % 1000 == 0:
                print(count)
            cleaned.append(clean_tweet(t))
        '''

        df = pd.DataFrame(cleaned)
        df.to_csv('./data/test/frenchtweets_test.csv', index=False, sep=" ", header=None, encoding='UTF-8')

def clean_train():
    INTPUT_FILE = '../data/train/tweets.csv'
    OUTPUT_FILE = '../data/train/tweets_cleaned.csv'

    print("Cleaning training file ...")

    with open(INTPUT_FILE, 'r', newline='\n', encoding='UTF-16') as csvinfile:
        csv_reader = csv.reader(csvinfile, delimiter=',')
        label = []
        text = []
        count = -1
        for row in csv_reader:
            # Dirty trick to skip headers
            if count == -1:
                count = 0
                continue
            if row is not None and len(row) == 2 and str(row[0]) in ['0', '2', '4']:
                if count != 0 and count % 1000 == 0:
                    print(count)

                label.append(transform_label(str(row[0])))
                text.append(clean_tweet(str(row[1])))
                # data.append(transform_label(str(row[0])))
                # data.append(clean_tweet(str(row[1])))
                # print(str(df_out.label.iat[-1]) + " " + str(df_out.text.iat[-1]))
                count += 1

        df_out = pd.DataFrame({'label': label, 'text': text})
        df_out.to_csv(OUTPUT_FILE, index=False, sep=',', header=False, encoding='UTF-8')
        print("File created")

'''
def clean_train3():
    INTPUT_FILE = '../data/train/tweets.csv'
    OUTPUT_FILE = '../data/train/tweets_cleaned.csv'

    print("Cleaning training file ...")

    with open(OUTPUT_FILE, 'w', encoding='UTF-8') as csvoutfile:
        csv_writer = csv.writer(csvoutfile, delimiter=' ', lineterminator='\n')
        with open(INTPUT_FILE, 'r', encoding='UTF-16') as csvinfile:
            csv_reader = csv.reader(csvinfile, delimiter=',')
            count = 0
            for row in csv_reader:
                if row is not None and len(row) >= 2 and str(row[0]) in ['0', '2', '4']:

                    if count != 0 and count % 100 == 0:
                        print(count)
                        break
                    cur_row = []
                    cur_row.append(transform_label(str(row[0])))
                    cur_row.append(clean_tweet(str(row[1:])))
                    csv_writer.writerow(cur_row)
                    count += 1

    print("File created")

def clean_train2():
    INTPUT_FILE = '../data/train/tweets.csv'
    OUTPUT_FILE = '../data/train/tweets_cleaned.csv'

    print("Cleaning training file ...")

    df_out = pd.DataFrame({'label': [],'text': []})

    with open(INTPUT_FILE, 'r', newline='\n', encoding='UTF-16') as csvinfile:
        csv_reader = csv.reader(csvinfile, delimiter=',')
        data = {'label': [],'text': []}
        count = -1
        for row in csv_reader:
            # Dirty trick to skip headers
            if count == -1:
                count = 0
                continue
            if row is not None and len(row) == 2 and str(row[0]) in ['0', '2', '4']:
                if count != 0 and count % 1000 == 0:
                    print(count)

                df_out = df_out.append({'label': transform_label(str(row[0])), 'text': clean_tweet(str(row[1]))}, ignore_index=True)
                #df_out['label'] = transform_label(str(row[0]))
                #df_out['text'] = clean_tweet(str(row[1]))

                #data.append(transform_label(str(row[0])))
                #data.append(clean_tweet(str(row[1])))
                #print(str(df_out.label.iat[-1]) + " " + str(df_out.text.iat[-1]))
                count += 1
                #print("loop")

                # TODO: using matrix/np.array and fill frames
                # temp = pd.DataFrame({'label': pd.Series(transform_label(str(row[0]))), 'text': pd.Series(clean_tweet(str(row[1])))})
                # df_out = pd.concat([df_out, temp])

        #d = {labels: tweets}
        #df_out = df_out.append(d, ignore_index=True)
        df_out.to_csv(OUTPUT_FILE, index=False, sep=',', header=False, encoding='UTF-8')
        print("File created")

def clean_train():
    INTPUT_FILE = '../data/train/tweets.csv'
    OUTPUT_FILE = '../data/train/tweets_cleaned.csv'

    print("Cleaning training file ...")

    col = ['label', 'text']
    df_in = pd.read_csv(INTPUT_FILE, encoding="utf-16", names=col, dtype={'label': np.float, 'text': np.str}, skiprows=1, nrows=1040)
    #squeeze=True
    df_out = pd.DataFrame(columns=col)
    count = 0
    for index, row in df_in.iterrows():
        print("Label:" + str(row[0]))
        print("Text:" + str(row[1]))
        if not row.empty and str(row[0]) in ['0', '2', '4']:
            count += 1

            if count % 1000 == 0:
                print(count)
            df_out['label'] = transform_label(str(row[0]))
            df_out['text'] = clean_tweet(str(row[1]))

    df_out.to_csv(OUTPUT_FILE, index=False, sep=" ")
'''

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

if __name__ == "__main__":
    clean_train()
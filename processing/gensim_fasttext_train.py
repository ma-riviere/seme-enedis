import datetime
import os

import fastText
from gensim.models.fasttext import FastText as ft

MODEL2 = "../model/fr.bin"
MODEL_VEC = "../model/fr.vec"

TRAIN = '../data/tweets.train'
TEST = '../data/tweets.test'
VALID = '../data/tweets.validation'
MODEL_PATH = '../data/'
MODEL_NAME = 'twitter_sa'

gmodel = ft.load_fasttext_format(MODEL2)
#model = fastText.load_model(MODEL2)
#vec = fastText.load_model(MODEL_VEC)

def train():
    print('Training start')
    try:
        hyper_params = {"lr": 0.01,
                        "epoch": 2,
                        "wordNgrams": 2,
                        "dim": 10}

        print(str(datetime.datetime.now()) + ' START=>' + str(hyper_params))

        # Train the model.
        trained = fastText.train_supervised(input=TRAIN, pretrainedVectors=gmodel, **hyper_params)
        print("Model trained with the hyperparameter \n {}".format(hyper_params))

        # CHECK PERFORMANCE
        print(str(datetime.datetime.now()) + 'Training complete.' + str(hyper_params))

        '''
        model_acc_training_set = model.test(TRAIN)
        print("Testing on training data done")
        model_acc_validation_set = model.test(VALID)
        print("Testing on validation data done")

        # DISPLAY ACCURACY OF TRAINED MODEL
        text_line = str(hyper_params) + ",accuracy:" + str(model_acc_training_set[1]) + ", validation:" + str(
            model_acc_validation_set[1]) + '\n'
        print(text_line)

        model.save_model(os.path.join(MODEL_PATH, MODEL_NAME + ".bin"))
        '''
        # quantize a model to reduce the memory usage
        trained.quantize(input=TRAIN, qnorm=True, retrain=True, cutoff=100000)
        print("Model is quantized!!")
        trained.save_model(os.path.join(MODEL_PATH, MODEL_NAME + ".ftz"))

        #print("Testing")
        #model.predict(['Pourquoi pas'], k=3)
        #model.predict(["C'est tellement mauvais"], k=1)

    except Exception as e:
        print('Exception during training: ' + str(e))

if __name__ == "__main__":
    train()
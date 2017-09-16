import numpy as np
import random
import operator
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import TimeDistributed
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.models import load_model

import re, string

def main(pathname):
    reason = []
    with open(pathname, "r") as f:
        lines = f.readlines()
        for line in lines:
            word_list = line.split()
            for item in word_list:
                item = item.lower()
                exclude = set(string.punctuation)
                item = ''.join(ch for ch in item if ch not in exclude)
            reason.extend(word_list)

    model = load_model("../../model.hdf5")

    word_to_num = {}
    with open("dict.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            word = tokens[0].lower()
            exclude = set(string.punctuation)
            item = ''.join(ch for ch in word if ch not in exclude)
            word_to_num[item] = int(tokens[1])

    X_input = [[word_to_num[i.lower()] for i in reason]]
    X_input = sequence.pad_sequences(X_input, 12)
    arr = model.predict(X_input)

    if arr[0][1] > arr[0][0]:
        return 1
    else:
        return 0

main("reason.txt")

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

import re, string

def generate_dataset():
    reasons = []
    with open("./data/reasondb.txt") as f:
        lines = f.readlines()
        for line in lines:
            word_list = line.split()
            for item in word_list:
                item = item.lower()
                exclude = set(string.punctuation)
                item = ''.join(ch for ch in item if ch not in exclude)
            reasons.append(word_list)

    flat_list = [item for sublist in reasons for item in sublist]
    flat_prob = []
    word_set = list(set(flat_list))
    for i in range(len(word_set)):
        prob = random.uniform(0.0, 1.0)
        flat_prob.append(prob)
    prob_dict = dict((k, v) for (k, v) in zip(word_set, flat_prob))
    # print(prob_dict)
    data_pts = []
    f = open("./data/data.txt", "w")
    for j in range(10000):
        data_pt = []
        for i in range(4):
            seq_len = np.random.randint(2, 4)
            item = reasons[np.random.randint(len(reasons) - 1)]
            start_ix = np.random.randint(len(item) - seq_len + 1)
            data_pt.extend(item[start_ix : start_ix + seq_len])
        total_prob = 0.0
        for word in data_pt:
            total_prob += prob_dict[word]
        total_prob /= len(data_pt)
        data_pt.append(total_prob)
        data_pts.append(data_pt)
        for p in data_pt:
            f.write(str(p) + " ")
        f.write("\n")
    f.close()


def train():
    reasons = []
    labels = []
    with open("./data/data.txt") as f:
        lines = f.readlines()
        for line in lines:
            word_list = line.split()
            label = word_list[-1]
            word_list = word_list[:-1]
            for item in word_list:
                item = item.lower()
                exclude = set(string.punctuation)
                item = ''.join(ch for ch in item if ch not in exclude)
            reasons.append(word_list)
            label = float(label)
            if label > 0.5:
                label = 1
            else:
                label = 0
            labels.append(label)

    # print(reasons)
    # print(labels)

    flat_list = [item for sublist in reasons for item in sublist]
    num_to_word = dict((k, v) for (k, v) in enumerate(set(flat_list)))
    word_to_num = dict((v, k) for (k, v) in enumerate(set(flat_list)))
    with open("dict.txt", "w") as f:
        for key, item in word_to_num.items():
            f.write(str(key) + " " + str(item) + "\n")
    num_flat_list = [word_to_num[item] for item in flat_list]

    num_features = len(set(flat_list))

    X_train = []
    y_train = []
    X_test = []
    y_test = []

    for reason, label in zip(reasons, labels):
        train_or_test = random.uniform(0.0, 1.0)
        if train_or_test > 0.2:
            X_train.append([word_to_num[item] for item in reason])
            if label == 1:
                y_train.append([0, 1])
            else:
                y_train.append([1, 0])
        else:
            X_test.append([word_to_num[item] for item in reason])
            if label == 1:
                y_test.append([0, 1])
            else:
                y_test.append([1, 0])

    max_reason_length = max([len(X) for X in X_train])
    X_train = sequence.pad_sequences(X_train, maxlen=max_reason_length)
    # y_train = to_categorical(y_train, nb_classes=10)
    # y_test = to_categorical(y_train, nb_classes=10)
    embedding_vector_length = 32
    model = Sequential()
    model.add(Embedding(len(flat_list), embedding_vector_length, input_length=max_reason_length))
    model.add(Dropout(0.2))
    model.add(LSTM(30))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    print(model.summary())
    model.fit(X_train, y_train, epochs=4, batch_size=64)


    X_test = sequence.pad_sequences(X_test, maxlen=max_reason_length)
    pred = model.predict(X_test, verbose=0)

    total = 0
    correct = 0
    for p, l in zip(pred, y_test):
        if l[max(enumerate(p), key=operator.itemgetter(1))[0]] == 1:
            correct += 1
        total += 1

    print("Accuracy:" + str(correct / total))
    print(len(X_test))
    print(len(X_train))

    model.save("model.hdf5")

    # X = []
    # for reason in reasons:
    #     X.append([word_to_num[item] for item in reason])
    # max_reason_length = max([len(r) for r in X])
    # print(max_reason_length)
    # X = sequence.pad_sequences(X, maxlen=max_reason_length, value=np.random.randint(num_features))

    # X_train = np.zeros((len(num_flat_list) - max_reason_length - 2, max_reason_length - 1, num_features))
    # y_train = np.zeros((len(num_flat_list) - max_reason_length - 2, max_reason_length - 1, num_features))
    # for i in range(len(X)):
    #     # seq = num_flat_list[i: i + max_reason_length]
    #     seq = X[i]
    #     # X_seq = seq
    #     X_seq = seq[:-1]
    #     # y_seq = num_flat_list[i + 1: i + max_reason_length + 1]
    #     y_seq = seq[1:]
    #     input_seq = np.zeros((max_reason_length - 1, num_features))
    #     for j in range(max_reason_length - 1):
    #         input_seq[j][X_seq[j]] = 1
    #     X_train[i] = input_seq

    #     target_seq = np.zeros((max_reason_length - 1, num_features))
    #     for j in range(max_reason_length - 1):
    #         target_seq[j][y_seq[j]] = 1
    #     y_train[i] = target_seq

    # def generate_text(model, length):
    #     ix = [np.random.randint(num_features)]
    #     y_words = [num_to_word[ix[-1]]]
    #     X = np.zeros((1, length, num_features))
    #     for i in range(length):
    #         X[0, i, :][ix[-1]] = 1
    #         print(num_to_word[ix[-1]], end=" ")
    #         ix = np.argmax(model.predict(X[:, :i + 1, :])[0], 1)
    #         y_words.append(num_to_word[ix[-1]])
    #     return (" ").join(y_words)

    # model = Sequential()
    # model.add(LSTM(max_reason_length - 1, input_shape=(None, num_features), return_sequences=True))
    # # for i in range(4):
    # #     model.add(LSTM(max_reason_length - 1, return_sequences=True))
    # model.add(TimeDistributed(Dense(num_features)))
    # model.add(Activation("softmax"))
    # model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    # epoch = 0
    # while epoch < 50:
    #     print("Epoch: ", epoch)
    #     model.fit(X_train, y_train, batch_size=8, verbose=1, epochs=1)
    #     print(generate_text(model, max_reason_length - 1))
    #     if epoch % 10 == 0:
    #         model.save_weights("checkpoint_{}_epoch_{}.hdf5".format(5, epoch))
    #     epoch += 1


def main():
    generate_dataset()
    train()


if __name__ == "__main__":
    main()

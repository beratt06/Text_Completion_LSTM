#Ä°mport Libraries
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM , Dense , Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

#Create Dataset from GPT
Texts = pd.read_csv("Text_LSTM.csv")
Texts = Texts["Text"].tolist()

#Tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts(Texts)
total_words = len(tokenizer.word_index) +1

# Text Sorting and padding
input_sequences = []
for text in Texts:
    token_list = tokenizer.texts_to_sequences([text])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)
max_sequence_length = max(len(x) for x in input_sequences)
input_sequences = pad_sequences(input_sequences,maxlen=max_sequence_length,padding="pre")

X, y =input_sequences[:,:-1], input_sequences[:,-1]
y = tf.keras.utils.to_categorical(y,num_classes=total_words)

#Create LSTM Model
model = Sequential()
model.add(Embedding(total_words , 50 , input_length = X.shape[1]))
model.add(LSTM(200, return_sequences=False))
model.add(Dense(total_words, activation="softmax"))

model.compile(optimizer="adam" , loss="categorical_crossentropy" , metrics=["accuracy"])

#Train Model
model.fit(X,y,epochs=100 , verbose=1)

#Evaluation
def predict_next_Word(send_text , next_words):
    
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([send_text])[0]
        token_list = pad_sequences([token_list],maxlen=max_sequence_length-1 , padding="pre")
        predicted_probs = model.predict(token_list, verbose=0)
        predicted_Word_index = np.argmax(predicted_probs, axis=1)
        predicted_Word = tokenizer.index_word[predicted_Word_index[0]]
        send_text = send_text + " " +predicted_Word
        
    return send_text

send_text = "Sabah Yürüyüşünde"
print(predict_next_Word(send_text, 7))
    
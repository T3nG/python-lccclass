#將 w2v_model, training.16000000...csv copy 到本專案中
#pip install tensorflow==2.10.1 scikit-learn nltk gensim xlrd openpyxl pandas
import os.path
import pickle
import re
import shutil
import time
from collections import Counter

import pandas as pd
import nltk
from gensim.models import Word2Vec
from keras import Sequential
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.layers import Embedding, Dropout, LSTM, Dense
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
#文字預處理, 將連結, 標點符號，及停用詞刪除
def preprocess(text):
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower().strip())
    tokens=[]
    for word in text.split():#字串轉 list
        if word not in stop_words:
            tokens.append(word)
    return " ".join (tokens)#list 轉字串
def decode_sentiment(label):
    return decode_map[int(label)]

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None


cols = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"
print("讀取資料....")
t1=time.time()
df=pd.read_csv('training.1600000.processed.noemoticon.csv',
               encoding=DATASET_ENCODING, names=cols)
t2=time.time()
print(f"讀取資料花費時間: {t2-t1}秒")

nltk.download('stopwords')
stop_words=stopwords.words("english")
decode_map={0:"NEGATIVE",2:"NEUTRAL",4:"POSITIVE"}
print("轉成 negative positive....")
t1=time.time()
df.target=df.target.apply(lambda x:decode_sentiment(x))
t2=time.time()
print(f"轉換花費時間: {t2-t1}秒")
target_cnt = Counter(df.target)
#預處理，請除不要的文字，包含停用詞
print('開始預處理.....')
t1=time.time()
df.text=df.text.apply(lambda x:preprocess(x))
t2=time.time()
print(f"預處理花費時間: {t2-t1}秒")
#print(df)

#train_test_split為 scikit-learn提供拆開訓練及測試用的函數
#random_state : 種下種子，讓每次產生的亂數都一樣，方便開發時期除錯用
#待開發完成後，即可移除
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
#print(df_train.shape, df_test.shape)
#把 tokenizer想成是一部字典
tokenizer=Tokenizer()#目前為空字典
print('開始製作字典....')
t1=time.time()
tokenizer.fit_on_texts(df_train.text)#製作單字的編碼
x_train=pad_sequences(tokenizer.texts_to_sequences(df_train.text), maxlen=300)#把每個句子變成同樣的長度
x_test=pad_sequences(tokenizer.texts_to_sequences(df_test.text), maxlen=300)
t2=time.time()
print(f"製作字典花費時間: {t2-t1}秒")
#儲存字典
pickle.dump(tokenizer, open("eng_dictionary.pkl", "wb"), protocol=0)#protocol=0 覆寫舊的資料

#開始準備訓練的資料
labels=df_train.target.unique().tolist()
labels.append("NEUTRAL")

encoder=LabelEncoder()
encoder.fit(df_train.target.tolist())
y_train=encoder.transform(df_train.target.tolist())
y_test=encoder.transform(df_test.target.tolist())
#轉成 n*1的維度
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)


vocab_size=len(tokenizer.word_index)+1
#產生(vocab_size, 100)的二維陣列，100表示 100 個維度的向量值，也就是說每個字有 100 個特徵
embedding_matrix=np.zeros((vocab_size, 100))
w2v_model=Word2Vec.load("w2v_model")
for word, i in tokenizer.word_index.items():
    if word in w2v_model.wv:
        embedding_matrix[i]=w2v_model.wv[word]#取得word這個字在 w2v_model裏的權重(向量值)
model=Sequential()
model.add(Embedding(
    vocab_size,
    100,#每個字有100個向量值
    weights=[embedding_matrix],
    input_length=300,
    trainable=False
))
model.add(Dropout(0.5))#隨機去除50%神經元的值，增加訓練的混雜度
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss='binary_crossentropy',#二元交叉熵
              optimizer="adam",
              metrics=['accuracy']
              )
#回調函數
#ReduceLROnPlateau : Reduce Learning Rate:
#模型訓練時，學習率大都固定。用 Reduce，可以動態縮小學習率，有助於找到最佳解
#EarlyStopping : 用於提前停止訓練，當訓練的 loss 不再減小，就停止訓練
callbacks=[ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
           EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)]
print("開始訓練......")
t1=time.time()
history=model.fit(x_train, y_train,
                  batch_size=1024,
                  validation_split=0.1,
                  verbose=1,#可以看到訓練的進度
                  validation_data=(x_test, y_test),
                  callbacks=callbacks
                  )
t2=time.time()
print(f"訓練時間花費 : {t2-t1}秒")
score=model.evaluate(x_test, y_test, batch_size=1024)
print(f"Accuracy:{score[1]}")
print(f"Loss:{score[0]}")
acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['acc_loss']
epochs=range(len(acc))
import pylab as plt
plt.legend()
plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
if os.path.exists("sentiment_model"):
    shutil.rmtree("sentiment_model")
model.save("sentiment_model")
plt.show()
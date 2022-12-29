# 將 w2v_model, training.16000000...csv copy 到本專案中
# pip install tensorflow==2.10.1 scikit-learn nltk gensim xlrd openpyxl pandas matplotlib
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import pickle
import re
import shutil
import time
from collections import Counter

import numpy as np
import pandas as pd
import pylab as plt
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

TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
# 文字預處理, 將連結, 標點符號，及停用詞刪除


def preprocess(text):
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower().strip())
    tokens=[]
    for word in text.split():  # 字串轉 list
        if word not in stop_words:
            tokens.append(word)
    return " ".join (tokens)  # list 轉字串


def decode_sentiment(label):
    return decode_map[int(label)]


display = pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None


cols = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"
print("讀取資料....")
t1 = time.time()
df = pd.read_csv('training.1600000.processed.noemoticon.csv',
               encoding=DATASET_ENCODING, names=cols)
t2 = time.time()
print(f"讀取資料花費時間: {t2-t1}秒")

nltk.download('stopwords')
stop_words = stopwords.words("english")
decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}
print("轉成 negative positive....")
t1 = time.time()
df.target = df.target.apply(lambda x: decode_sentiment(x))
t2 = time.time()
print(f"轉換花費時間: {t2-t1}秒")
target_cnt = Counter(df.target)
# 預處理，清除不要的文字，包含停用詞
print('開始預處理.....')
t1 = time.time()
df.text = df.text.apply(lambda x: preprocess(x))
t2 = time.time()
print(f"預處理花費時間: {t2-t1}秒")
# print(df)

# train_test_split為 scikit-learn提供拆開訓練及測試用的函數
# random_state : 種下種子，讓每次產生的亂數都一樣，方便開發時期除錯用
# 待開發完成後，即可移除
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
# print(df_train.shape, df_test.shape)
# 把 tokenizer想成是一部字典
tokenizer = Tokenizer()  # 目前為空字典
print('開始製作字典....')
t1 = time.time()
tokenizer.fit_on_texts(df_train.text)  # 製作單字的編碼
x_train = pad_sequences(tokenizer.texts_to_sequences(df_train.text), maxlen=300)  # 把每個句子變成同樣的長度
x_test = pad_sequences(tokenizer.texts_to_sequences(df_test.text), maxlen=300)  # 把每個句子變成同樣的長度
t2 = time.time()
print(f"製作字典花費時間: {t2-t1}秒")
# 儲存字典
pickle.dump(tokenizer, open('eng_dictionary.pkl', 'wb'), protocol=0)  # protocol=0 覆寫舊的資料

# 開始準備訓練的資料
labels = df_train.target.unique().tolist()
labels.append('NEUTRAL')

encoder = LabelEncoder()
encoder.fit(df_train.target.tolist())  # df_train 跟 df_test 是從 train_test_split 分割而來, 結構是一樣的
y_train = encoder.transform(df_train.target.tolist())
y_test = encoder.transform(df_test.target.tolist())
# 轉成 n*1的維度, 前面兩維相乘
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

vocab_size = len(tokenizer.word_index)+1
# 產生(vocab_size, 100)的二維陣列, 100表示 100個維度的向量值, 也就是說每個字有 100個特徵的意思
embedding_matrix = np.zeros((vocab_size, 100))
w2v_model = Word2Vec.load('w2v_model')
for word, i in tokenizer.word_index.items():
    if word in w2v_model.wv:
        embedding_matrix[i] = w2v_model.wv[word]  # 取得每個 word在 w2v_model裡的權重(向量值)
# print(f'x_test_len: {len(x_test)}\ny_test_len: {len(y_test)}')
# print(f'x_test: \n{x_test}\ny_test: \n{y_test}')

model = Sequential()
model.add(Embedding(
    vocab_size,
    100,  # 每個字有 100個向量值
    weights=[embedding_matrix],
    input_length=300,
    trainable=False  # 以embedding_matrix 提供的權重就好, 不須再訓練
))
model.add(Dropout(0.5))  # 隨機去除 50%神經元的值, 增加訓練的混雜度
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(
    loss='binary_crossentropy',  # 二元交叉熵
    optimizer='adam',
    metrics=['accuracy']
)
# 回調函數
# ReduceLROnPlateau: Reduce Learning Rate
# 模型訓練時, 學習率大都固定, 用 Reduce可以動態縮小學習率, 有助於找到最佳解
# EarlyStopping 用於提前停止訓練, 當訓練的 loss不再減少, 就停止訓練
callbacks = [
    ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
    EarlyStopping(monitor='val_accuracy', min_delta=1e-4, patience=5)
]
print('開始訓練....')
t1 = time.time()
history = model.fit(
    x_train,
    y_train,
    batch_size=1024,  # 依顯卡RAM調整
    epochs=8,
    validation_split=0.1,  # 訓練中的驗證: 90%訓練 10%驗證
    verbose=1,  # 可以看到目前訓練的進度
    validation_data=(x_test, y_test),
    callbacks=callbacks
)
t2 = time.time()
print(f'訓練時間花費: {t2-t1}秒')
score = model.evaluate(x_test, y_test, batch_size=1024)
print(f'Accuracy: {score[1]}')
print(f'Loss: {score[0]}')
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))
plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.plot(epochs, loss, 'royalblue', label='Training loss')
plt.plot(epochs, val_loss, 'crimson', label='Validation loss')
plt.title('Training and validation accuracy/loss')
plt.legend()
if os.path.exists('lasttime/my_sentiment_model'):
    shutil.rmtree('lasttime/my_sentiment_model')
model.save('my_sentiment_model')
plt.savefig('result.png')
plt.show()
# plt.legend() : position change
# model.fit : add epoch=8
# callbacks EarlyStopping : val_accuracy

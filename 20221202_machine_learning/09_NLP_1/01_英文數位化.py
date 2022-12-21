# pip install tensorflow==2.10.1 scikit-learn nltk gensim xlrd openpyxl pandas
# nltk: tokenizer 將抓到的字詞編成字典, 且轉成自己的編碼
# genism: 向量化模型 => this :[0.12, 0.35, 0.56]
# 實際上genism, 向量化並不是三維, 而是100維, 計算100維的直線距離
# 文章資料下載 (200多MB)
# https://storage.googleapis.com/kaggle-data-sets/2477/4140/compressed/training.1600000.processed.noemoticon.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221221%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221221T112449Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=007d00e455058daf15158a6f383109aeabdce25f3239920a1ead509ad345cd176a00b51253d1ab2effcf343120ea40ed30d6392a5ae6b717f4ec9210b6231f3b3c3867824fe99e215604a70a5daf8d1103fac11c8e2ac757487912f7a010f813047cdb7d937d79741c864d46af2c53584f1e9699e249c47d6a896d1eb17328d02d67fd51879766f25b747e0ba8be1ac7201e68c2de4aede9a901561b1dbf041067d87b52c1c8d017ba26c63d45f7ca5b043d3c5b91eaf13adb5e01c26bbe5fedc721cd1e6924ce7f29f6357258abe51f16d0785b97678f3ffe4bee9cdc3fec9b7d7eefe43b299a43ede32855d0227a4d0fc9616b2a8a64ddd72292984ad90468
# C:\Users\User\AppData\Roaming\nltk_data
import re
import time

import nltk
import pandas as pd
from gensim.models import Word2Vec
from nltk.corpus import stopwords

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

def preprocess(text):
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower().strip())
    tokens = []
    for word in text.split():
        if word not in stop_words:
            tokens.append(word)
    return " ".join(tokens)

DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"

df = pd.read_csv(
    'training.1600000.processed.noemoticon.csv',
    encoding=DATASET_ENCODING,
    names=DATASET_COLUMNS
)
# 約有160萬筆資料, 每筆有6個欄位
# 第0個欄位(target): 0 正評, 4: 負評
# print(df)
print(df.shape)

# 下載停用詞
nltk.download('stopwords')
stop_words = stopwords.words("english")
# print(stop_words)

# 開始預處理
# lambda 匿名函數
# 返回值: 要處理的事情(只能有一行)
print(f'開始預處理.....')
t1 = time.time()
df.text = df.text.apply(lambda x:preprocess(x))
t2 = time.time()
print(f'預處理時間: {t2-t1}秒')
# x = preprocess("I am this book")
# print(x)
# print(df.text)

# 將每個句子拆開成單字集合, 為二維的結構
# [['thanks', 'eastwestchic', 'amp', 'wangyip', 'thanks', 'looking'],
#  ['thanks', 'martin', 'imaginative', 'interface'],
# ...]

vocabularies = [sentence.split() for sentence in df.text]
print(f'vocabularies的數量: {len(vocabularies)}')
w2v_model = Word2Vec(
    window=7,  # 與前7後7個字產生關聯
    min_count=10,  # 總出現次數小於10次就去除掉
    workers=8  # 要用幾個執行緒去執行
)
# 建立Word2Vec的單字, 變成一部字典, 才能進行訓練, 此字典儲存在 w2v_model模型中
w2v_model.build_vocab(vocabularies)
# 新版本使用以下方式
words = list(w2v_model.wv.key_to_index.keys())
# 舊版本需使用如下方式
# words = w2v_model.wv.vocab.keys()
vocab_size = len(words)
print(f'單字數: {vocab_size}')  # 34515
print("開始向量化.....")
t1=time.time()
w2v_model.train(vocabularies, total_examples=len(vocabularies), epochs=32)
t2=time.time()
print(f'向量化時間: {t2-t1}秒')
w2v_model.save('w2v_model')
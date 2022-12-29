# pip install gensim tensorflow==2.10.1 nltk xlrd openpyxl pandas scikit-learn
import codecs
import re
import time

import jieba
from gensim.models import Word2Vec


def preprocess(txt):
    txt = re.sub(TEXT_CLEANING_RE, ' ', str(txt).lower()).strip()
    return txt.replace(' ', '')


TEXT_CLEANING_RE = "[0-9a-zA-Z,:.?!\"\+\-*/_='()\[\]|<>$（）［］，｜、《》！？”%【】“　．…❤️：]"

with open('stops.txt', 'r', encoding='utf-8') as f:
    stops = f.read().split('\n')
file = codecs.open('train_ts.csv', 'r', 'utf-8')
jieba.set_dictionary('dict.txt')
print('開始做結巴斷詞...')
vocabularies = []
result = []
for line in file.readlines():
    # 取得最後一個欄位的資料, unrelated, agree, disagree
    s = line.split(',')
    result.append(s[len(s)-1])

    line = preprocess(line)
    terms = [t for t in jieba.cut(line, cut_all=True) if t not in stops]  # 斷詞
    vocabularies.append(terms)

# load model, word to vector
w2v_model = Word2Vec(
    window=7,  # 前後7個字列入相關
    min_count=10,
    workers=8
)
print('開始製作w2v_model字詞...')
w2v_model.build_vocab(vocabularies)
# 新版把字詞放到 wv中, 網路上大都是舊版 Word2Vec教學, 無法相容
words = list(w2v_model.wv.key_to_index.keys())
vocab_size = len(words)
print(f'vocab_size: {vocab_size}')
print('開始向量化...')
t1 = time.time()
w2v_model.train(
    vocabularies,
    total_examples=len(vocabularies),
    epochs=32
)
t2 = time.time()
print(f'向量化時間: {t2-t1}秒')
w2v_model.save('w2v_model_cht')
rs = w2v_model.wv.most_similar('美國')
for r in rs:
    print(r)

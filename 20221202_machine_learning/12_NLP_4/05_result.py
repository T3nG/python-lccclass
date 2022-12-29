from gensim.models import Word2Vec

# 欲偵測的字詞
txt = '天災'

model = Word2Vec.load('w2v_model_cht')
try:
    rs = model.wv.most_similar(txt)
    for r in rs:
        print(r)
except:
    print('無相關詞彙')

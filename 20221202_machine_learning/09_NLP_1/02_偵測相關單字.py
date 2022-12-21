from gensim.models import Word2Vec

words = ['Love', 'Taiwan']
model = Word2Vec.load("w2v_model")
for word in words:
    rs = model.wv.most_similar(word.lower())
    print(f'========{word}========')
    for r in rs:
        print(r)
    print()

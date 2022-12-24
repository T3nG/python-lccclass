from keras_preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder

planet = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Earth']
encoder = LabelEncoder()
encoder = encoder.fit(planet)  # 過濾重複及給予編號
x = encoder.transform(planet)  # 將單字以編號列出
print(x)  # 一維陣列, 從 0開始
# [3 5 0 2 1 4 0]
print(encoder.fit_transform(planet))

tokenizer = Tokenizer()
tokenizer.fit_on_texts(planet)
print(tokenizer.word_index)
# {'earth': 1, 'mercury': 2, 'venus': 3, 'mars': 4, 'jupiter': 5, 'saturn': 6}
print(tokenizer.texts_to_sequences(planet))  # 二維 list, 從 1開始
# [[2], [3], [1], [4], [5], [6], [1]]

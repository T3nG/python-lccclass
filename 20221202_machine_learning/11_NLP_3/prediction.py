# pip install tensorflow==2.10.1 scikit-learn
import os
import pickle
import keras
from keras_preprocessing.sequence import pad_sequences

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 官網有錯誤的地方
# https://www.kaggle.com/code/paoloripamonti/twitter-sentiment-analysis
def get_label(score):
    label = '中立'
    if score <= 0.4:
        label = '負評'
    elif score >= 0.7:
        label = '正評'
    return label

# 載入字典 eng_dictionary.pkl
with open('eng_dictionary.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
# 載入模型
model = keras.models.load_model('my_sentiment_model')

txt = 'I love music'
# 'John is a bad guy', 'Tom is an asshole'
x_test = pad_sequences(tokenizer.texts_to_sequences([txt]), maxlen=300)
score = model.predict([x_test])[0][0]
#      score<0.4: 負評
# 0.4<=score<=0.7: 中立
#      score>0.7: 正評
label = get_label(score)
print(score, label)

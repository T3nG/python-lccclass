# 文字雲測試
# 開啟停用詞
from collections import Counter

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('stops.txt', 'r', encoding='utf-8') as f:
    # 使用 set會加速處理功能, 比 list快很多
    stops = set(f.read().split('\n'))
txt = ''
with open('wordcloud_test_data.txt', 'r', encoding='utf-8') as f:
    # 變成一整串
    txt = f.read().replace('\n', '')
    # txt = ' '.join(f.read().split('\n'))
    txt = txt.replace(' ', '').replace('/', '').replace('\"', '')

# 載入繁體中文字典
jieba.set_dictionary('dict.txt')
count = 15
num = len(stops)
terms = [t for t in jieba.cut(txt, cut_all=True) if t not in stops]
# print(Counter(terms))

# 文字雲處理
# 遮色片(mask)
# 使用小畫家畫一個心形形狀, 填入任何顏色, 背景使用白色
# 白色不顯示文字, 其他顏色區域才顯示文字
# 儲存成 heart.png
# 字型設定: 網路上都使用 simsun.ttf, 是錯的
from PIL import Image
import numpy as np
mask = np.array(Image.open('heart.png'))
word_cloud = WordCloud(font_path='simsun.ttc', background_color='white', mask=mask)
img = word_cloud.generate_from_frequencies(frequencies=Counter(terms))
plt.figure(figsize=(4,4))

# bilinear: 雙線性插值法, 讀文字不會有鋸齒狀
plt.imshow(img, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.png')
plt.show()


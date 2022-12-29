# 斷詞測試
# 開啟停用詞
import jieba

with open('stops.txt', 'r', encoding='utf-8') as f:
    stops = f.read().split('\n')
txt = '下雨天留客天天留我不留'
print('一般模式: ', [t for t in jieba.cut(txt)])
# 精準模式: 所有可能的斷詞都列出, 較為精準
print('精準模式: ', [t for t in jieba.cut(txt, cut_all=True)])


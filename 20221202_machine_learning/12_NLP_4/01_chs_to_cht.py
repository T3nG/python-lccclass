# 下載 langcon.py : http://mahaljsp.asuscomm.com/files/langconv.py
# 下載 zh_wiki.py : http://mahaljsp.asuscomm.com/files/zh_wiki.py
import codecs
import os

from langconv import Converter


def convert(target, ls):
    for l in ls:
        # 繁轉簡: 'zh-hans'
        # 簡轉繁: 'zh-hant'
        zhContent = Converter('zh-hant').convert(l)
        print(zhContent, end='')
        target.write(zhContent)


files = ['train', 'test']
count = []
for file in files:
    source = codecs.open(f'{file}.csv', 'r', 'utf-8')
    target = codecs.open(f'{file}_ts.csv', 'w', 'utf-8')
    ls = source.readlines()
    count.append(len(ls))
    convert(target, ls)
    target.close()
    source.close()
print(f'總共轉換筆數: {count}')
# 總共轉換筆數: [320767, 80133]

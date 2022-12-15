'''
DOM (Document Object Model) : 將XML解析成一棵樹, 效能差
SAX (Simple API for XML) : 使用事件驅動模型, 效能好, 占用記憶體少, 但不方便使用
ElementTree (元素樹) : 為上面二個的綜合體, 方便使用, 且效能跟SAX一樣, 且不占用太多的記憶體

'''

import xml.etree.ElementTree as ET

tree=ET.ElementTree(file="index.html")
root=tree.getroot()
# print(root.tag, root.attrib)
#<html>, <table> 標籤, tag "<> Diamond"

# for i in range(len(root)):
#     print(root[i].tag, root[i].attrib)
# root包含自己之外, 也包含了下一層的子標籤

# for node in root.iter():
#     print(node.tag, node.attrib)
# 每一層都列出來

# xpath: 使用絕對路徑, 由根開始指定要走的節點 body/table/tr
# node=tree.find('body/table/tr') # find: 找第一個, 傳回單一節點
# print(node.tag, node.attrib)

for node in tree.iterfind('body/table/tr'): # iterfind 找所有符合的, 以list傳回
    print(node.tag, node.attrib)

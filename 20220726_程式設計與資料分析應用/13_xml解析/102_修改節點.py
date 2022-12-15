# 修改節點時, 當然是要找到指定的節點

import xml.etree.ElementTree as ET

tree=ET.ElementTree(file="index.html")
root=tree.getroot()

node=tree.find('body/table/tr[@name="tr2"]/td')
node.set("bgcolor", "ffff00") # 設定屬性
node.text="中文測試"
tree.write('test.html') # 建立新檔案

import xml.etree.ElementTree as ET

html=ET.Element("html")
head=ET.Element("head")

title=ET.SubElement(head,"title")
title.text="as title"
body=ET.Element("body")

p=ET.SubElement(body,"p")
p.set("align","center")
p.text="My Web"

html.extend((head, body)) # 延伸, 建立父子關係
# tree=ET.ElementTree(html)
# tree.write("test.html")
# 列出來只有一整行, 看不懂

# 完美列印, 輸出有縮排的html檔案
from xml.dom import minidom
xmlstr = minidom.parseString(ET.tostring(html)).toprettyxml(indent="  ")
with open("test.html","w") as f:
    f.write(xmlstr)
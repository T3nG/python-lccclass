import xml.etree.ElementTree as ET

tree=ET.ElementTree(file="index.html")
root=tree.getroot()
table=tree.find("body/table")
tr=ET.SubElement(table, "tr") # 產生一個新的節點, 並附於node之下
td=ET.SubElement(tr, "td")
td.set("colspan","4")
td.text="新增的點"
tree.write("test.html")
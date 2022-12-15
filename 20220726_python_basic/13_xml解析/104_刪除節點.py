import xml.etree.ElementTree as ET

tree=ET.ElementTree(file="index.html")
root=tree.getroot()
table=tree.find("body/table")
tr=tree.find("body/table/tr[@name='tr2']")
table.remove(tr)
tree.write("test.html")
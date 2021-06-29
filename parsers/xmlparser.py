import os
from xml.etree import ElementTree

file="/home/rishabh/Desktop/Rishabh/seceon/sec2/file2.xml"
full_file=os.path.abspath(os.path.join("data",file))
print(full_file)

dom=ElementTree.parse(full_file)
print(dom)
print("End")

data=dom.findall('Hash')
print(data)
for d in data:
    print(d.text)
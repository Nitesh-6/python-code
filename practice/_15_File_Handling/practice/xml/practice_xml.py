import xml.etree.ElementTree as Et

tree = Et. parse("dummy.xml")
root = tree.getroot()

for ind in range(len(root)):
    print(root[ind].attrib)

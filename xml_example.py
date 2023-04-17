import xml.etree.ElementTree as ET

tree = ET.parse('xmlfile.xml')
root = tree.getroot()

item1 = ET.Element("item")
item1.text = "kuudes"
root.append(item1)
    
tree.write('xmlfile.xml')

import xml.etree.ElementTree as ET
tree = ET.parse('document.xml')
root = tree.getroot()

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

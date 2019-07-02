import xml.etree.ElementTree as ET
import os
import glob
import shutil
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

path = os.getcwd()
print(path)
os.chdir(path)
newpath=os.path

list_of_xmls = glob.glob(path+"//*.xml")
#name='demofile'

for item in list_of_xmls:
#	print(item)

#xml_raw = open("demofile.txt", "w") 
#l=[]

    with open(item) as f: root = ET.parse(f)
    xml_raw = open(item+".txt", "w") 
    for obj in root.findall('object'):
        bndbox: Element = obj.find('bndbox')
        name = obj.find('name').text
        xmin, xmax, ymin, ymax = [int(bndbox.find(x).text) for x in ['xmin', 'xmax', 'ymin', 'ymax']]
        coords = [(x, y) for x in [xmin, xmax] for y in [ymin, ymax]]
    #l.append(coords)

        print(coords, ','+name)
        xml_raw.write(str(coords)+str(',english')+'\n')
#print(l, name)


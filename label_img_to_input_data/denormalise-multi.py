import xml.etree.ElementTree as ET
import os
import glob
import shutil
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def extract_coords(list_of_xmls):
	for item in list_of_xmls:
		#print(item)

	#xml_raw = open("demofile.txt", "w") 
	#l=[]

	    with open(item) as f: root = ET.parse(f)
	    xml_raw = open(item+".txt", "w")

	    
	    for obj in root.findall('object'):
	    	#print(obj)
	    	bndbox: Element = obj.find('bndbox')
	    	name = obj.find('name').text
	    	xmin, xmax, ymin, ymax = [int(bndbox.find(x).text) for x in ['xmin', 'xmax', 'ymin', 'ymax']]
	    	coords = [(x, y) for x in [xmin, xmax] for y in [ymin, ymax]]
	    #l.append(coords)
	    	print(coords, ','+name)
	    	xml_raw.write(str(coords)+str(',english')+'\n')
	#print(l, name)


def remove_char(list_of_txt):
	for item in list_of_txt:
		output = open("temp.txt", "w")
		with open(item, 'r+') as f:
			for line in f.readlines():
				line = line.replace("[", "")
				line = line.replace("(", "")
				line = line.replace(")", "")
				line = line.replace("]", "")
				line = line.replace(" ", "")
				output.write(line)
		output.close()
		os.remove(item) # remove old file
		os.rename("temp.txt",item) # rename as old file


		#print(item)



path = os.getcwd()
print(path)
os.chdir(path)
newpath=os.path

list_of_xmls = glob.glob(path+"//*.xml")
extract_coords(list_of_xmls)

list_of_txt = glob.glob(path+"//*.txt")
remove_char(list_of_txt)

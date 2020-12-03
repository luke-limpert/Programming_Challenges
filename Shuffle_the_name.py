#Shuffle the name
import re
def name_shuffle(txt):
	return re.findall('\S*',txt)[2] + " " + re.findall('\S*',txt)[0]
name_shuffle("Rosie O'Donnell")
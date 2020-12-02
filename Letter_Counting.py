#challenge:

#Create a function that counts the number of x's and o's in a string and then 
#returns a True value if there are the same number of x's and o's in the string
#or if there are no x's and o's in the string. 

#If the number of x's and o's in the string differ return False.

def XO(txt):
	txt = txt.lower()
	countx = 0
	counto = 0
	for i in range(len(txt)):
		if txt[i] =="x":
			countx+=1
		elif txt[i] == "o":
			counto+=1
		else:
			continue
	if countx == counto:
		return True
	else:
		return False
print(XO("xxoox"))
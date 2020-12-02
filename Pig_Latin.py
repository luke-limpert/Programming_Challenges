x = "the 2 quick brown foxes"
y = x.split(sep=' ')
print(y)
count=0

for word in y:
	length = len(word)
	length+=1
	if word.isnumeric():
		y[count] = word[0]
	else:
		y[count] = word[1:length] + word[0] + "ay"
	count+=1

print(y)

def concat_piglatin(words):
	sentence = words
	count = 0
	j=""
	for i in words:
		j = j + i + " "
		count+=1
	return j

print(concat_piglatin(y))




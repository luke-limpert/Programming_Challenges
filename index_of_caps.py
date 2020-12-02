#index of caps challenge
def index_of_caps(word):
	count = 0
	lst = []
	for i in word:
		if i.isupper():
			lst.append(count)
		count += 1
	return lst
			

	
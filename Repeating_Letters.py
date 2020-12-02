def double_char(txt):
	lot = len(txt)
	output = ""
	for i in range(lot):
		output = output + txt[i] + txt[i]
	return output
	
#alternate solutions

#list comprehension method
# def double_char(txt):
# 	return ''.join(x*2 for x in txt)
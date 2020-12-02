def factorial(num):
	facto = 1
	for i in range(num+1):
		if i == 0:
			continue
		facto = i * facto
	return facto	
print(factorial(3))
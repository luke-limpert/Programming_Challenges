def add(n1, n2):	
	try:
		int(n1)
		int(n2)
		return str(eval(n1 + " + " + n2))
	except:
		return "Invalid Operation"
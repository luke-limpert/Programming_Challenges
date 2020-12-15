def not_good_math(n, k):
	for i in range(k):
		if str(n).endswith("0"):
			n/=10
			n = int(n)
			print(n)
		else:
			n-=1
			print(n)
	return n

print(not_good_math(78, 9))
#if the number ends in 0, divide by 10.
#if the number does not end in 0, subtract 1 from it
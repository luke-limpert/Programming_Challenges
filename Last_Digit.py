def last_dig(a, b, c):
	return True if (a%10 * b%10)==c%10 else False

print(last_dig(25, 21, 125))


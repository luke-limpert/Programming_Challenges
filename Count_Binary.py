#count 1's and 0's in the binary representation of a number
def count_ones(num):
	return [int(i) for i in str(bin(num).lstrip('0b'))].count(1)

print(count_ones(999))
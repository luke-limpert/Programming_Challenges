#max difference
#print the max difference between any 2 numbers
#in a sequence

#assumptions
#Each number is separated by a single space
# the numbers can be positive, zero, and negative

numbers = "1 9 2 -7 10 4 3"
numbers = numbers.split(" ")
print(numbers)

#loop through the list of random numbers and find the max difference
max = None
min = None
count=0
for i in numbers:
	numbers[count] = int(i)
	count+=1
print(numbers)

for j in numbers:
	if max==None and min==None:
		max = j
		min = j
	if max < j:
		max = j
	if min > j:
		min = j

print(abs(max - min))

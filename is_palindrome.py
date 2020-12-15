#palindrome challenge
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string = input_string.replace(" ", "").lower()
	# Traverse through each letter of the input string
	for i in range(len(input_string.strip())):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		
		new_string = new_string + input_string[i]
		reverse_string = input_string[i] + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
#how many vowels challenge
import re
def count_vowels(txt):
	return len(re.findall(r'[a]|[e]|[i]|[o]|[u]',txt))
print(count_vowels('Celebration'))
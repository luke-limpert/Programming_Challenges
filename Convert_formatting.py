def convert_to_number(dictionary):
	return_dict = {}
	for a, x in dictionary.items():
		return_dict[a] = int(x)
	return return_dict


print(convert_to_number({ "piano": "200", "tv": "300" }))
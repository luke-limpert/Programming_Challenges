def find_it(items, name):
	try:
		items[name]
		return name.capitalize() + " is gone..."
	except:
		return name.capitalize() + " is here!"

items = {"tv": 30, "timmy": 20, "stereo": 50,}
print(find_it(items, 'timmy'))
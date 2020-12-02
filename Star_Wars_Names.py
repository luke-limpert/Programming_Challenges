def relation_to_luke(name):
	names = {"Darth Vader": "father",
					"Leia": "sister",
					"Han": "brother in law",
					"R2D2": "droid"}
	return "Luke, I am your " + names[name] + "."
					
relation_to_luke("Darth Vader")
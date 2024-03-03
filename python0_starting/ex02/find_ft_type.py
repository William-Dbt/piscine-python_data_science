# Here I'll use the dictionnary variable to check if the type is know or not (matching the requirements of the exercice)
# We only want to check for list, tuple, set, dict and string
# We'll use the function .get of our dict to check if the type is what we search or not, if not just write "Type not found" and return 42
# If our type is known, we'll check for the str string ("X is in the kitchen"), or just print the type of the object as requested and return 0
# 
# For the joke, if nothing is send (0 chars) with the str one, I replace the string by "Nobody" (not asked)
def all_thing_is_obj(object: any) -> int:
	dict_types = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String"
	}

	objectType = type(object)
	if (dict_types.get(objectType) == None):
		print("Type not found")
		return 42
	elif (objectType == str):
		if (len(object) == 0):
			object = "Nobody"

		print(object + " is in the kitchen : " + str(objectType))
	else:
		print(dict_types[objectType] + " : " + str(objectType))

	return 0

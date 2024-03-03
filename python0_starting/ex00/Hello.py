ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# For a list, we can access to the element by his id (1 here for the second element of the list)
ft_list[1] = "World!"

# For a tuple, this structure is not mutable, it means that we can't write a value in it,
# We have to overwrite the original tuple by another one with our value
ft_tuple = (ft_tuple[0], "France!")

# For a set, we can use the function .discard or .remove to delete one object if it's equal to the argument given
# We have to use .add function to add something in the set, note that the variable to set have to be immutable and unique
# a set variable is unordered, it means that if you want to print the list, elements will not be in the order that you wrote in your code
ft_set.discard("tutu!")
ft_set.add("Paris!")

# For a dictionnary, we can grab the value that we want to modify by it's key as 'key : value'
# Each key must be unique.
# I used the function .get to check is the key "Hello" exists, it returns None if not
if (ft_dict.get("Hello") != None):
	ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
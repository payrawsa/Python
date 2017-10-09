print('hello!')
number= 3
string= "apple"
float = 1.2
def name_of_function(perm1, perm2):
	return perm1+perm2
# print(name_of_function(5,6))
# print(name_of_function(5.9,6.2))
# print(name_of_function("first, ", "Second"))

#ArrayList
list_Strings = ["mike", "alex", "troy", "dave"]

def loop_list(String_List):
	for item in String_List:
		print(item)

loop_list(list_Strings)

def range_loop():
	for i in range(0,10):
		print(i)
range_loop()

#HashMap
dict_string_int = {"Mike":6, "Alex":9, "Troy":99}

def value_of_dict(dictionary):
	for key in  dictionary:
		print(key)
		print(dictionary[key])
value_of_dict(dict_string_int)
if __name__ == "__main__":
	print("this is claled from the main function")
list_Strings.append("Billy")
print(list_Strings)

dict_string_int["Billy"]=84
print (dict_string_int)


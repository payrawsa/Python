#!/usr/bin/python

def Q1(number_list):
    return len(number_list)
    # TODO return number of ints in the list


def Q2(string_list):
    return string_list.append("movie")
    # TODO add the string "movie" to the end of the list and return that list
   

def Q3(number_list, index):
    return number_list[index]
    # TODO return the element at index i from the input list
    #      You can assume the input contains at least i+1 values
def Q4(number_list, value):
    if (value in number_list): 
        return True
    else:
        return False
    # TODO return true if value is in the input list, false otherwise


def Q5(string_list):
    return " ".join(string_list)
    # TODO return a string containing every word of the input concatenated into a single String and separated by spaces
    #      Example: If the input is ["war", "never", "changes"] the output is "war never changes"


def Q6():
    arraylist = [1,2,3,4,5,6,7,8,9,10]
    return arraylist
    # TODO Create and return an ArrayList of the integers 1 through 10 (including 1 and 10)


def Q7():
    arraylistnew = ["memory", "is", "the", "key"]
    return arraylistnew
    # TODO create and return an ArrayList of Strings containing the strings "memory", "is", "the", "key" in that order


def Q8(string_int_dict, key, value):
    string_int_dict[key] = value
    return string_int_dict[key]  
    # TODO  add an entry into the map with the the given key and value


def Q9(bool_int_dict, key):
    for key in bool_int_dict:
        return key
    # TODO return the value in the input map at the given key


def Q10(string_int_dict, value):
    if (value in string_int_dict):
        return True
    else:
        return False

    # TODO return true if value is in the input map as a value at any key, false otherwise


def Q11(string_double_dict):
    return len(string_double_dict)
    # TODO return the number of entries in the input map


def Q12(string_int_dict):
    return string_int_dict.values()
    # TODO return a list of all values in the input map


def Q13(string_int_dict):
    return string_int_dict.keys()
    # TODO return a list of all keys in the input map


def Q14(int_int_dict, key):
    if (key in int_int_dict.keys()):
        return True
    else:
        return False
    # TODO return true if key is a key in the input map, false otherwise


def Q15(int_int_dict, value):
    return int_int_dict.values().count(value)
    # TODO return the number of times value is in the input map as a value


if __name__ == "__main__":
    # execute only if run as a script
    our_list=[1,2,3]
    print(Q1(our_list))


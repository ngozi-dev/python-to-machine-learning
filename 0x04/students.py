#!/usr/bin/python3
# a module that reads a txt file

def students(filename): # declare a function with def
    new_dict = {} # open an empty dictionary called new_dict
    with open(filename, "r") as file: # read the file using content manager "with"
        content = file.readlines() # as you read this file line by line store it in a variable called content
        for name in content: # after reading this file, if the name is contained in the content
            key = name[0].upper() # the key value should be the first alphabet of the name and should be in capital letters
            value = new_dict.get(key) # the value 
            if value is None: # if value is not contained in the content
                new_dict[key] = [name.replace("\n","")]
            else:
                new_dict[key].append(name.replace("\n",""))
        return new_dict


if __name__ == "__main__":
    results = students("students.txt")
    print(results) 
            
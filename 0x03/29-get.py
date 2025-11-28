#!/usr/bin/python3
# a module that gets an item from a dictionary


# declared a dict called location and it contains keys and their values

location = {
    "south east": ["Enugu", "Anambra", "imo"],
    "south south": ["Edo", "Delta", "Bayelsa"],
    "south west": ["Lagos", "Ekiti", "Ogun"]
    
}

print(location)

# to extrct the values in a dict key you use 
# .get, open a bracket an spacify the value you want to get out
location.get("south east")
site = location.get("south east") # declare a variable site to accomodate the values
print(site)
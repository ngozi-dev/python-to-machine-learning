#!/usr/bin/python3
# a module that reads a txt file

def read_inventory(filename):
    inventory_dict = {}
    with open(filename, "r") as file:
        for line in file.readlines():
            clean_line = line.strip()
            if not clean_line:
                continue
            else:
                item,qty_str = clean_line.split(",")
                quantity = int(qty_str)
                inventory[item] = quantity
                return inventory

if __name__ == "__main__":
    result = read_inventory("inventory.txt")
    print(result)




#!/usr/bin/python3
# a module that tracks customers purchase in the supermarket

# Given data
customer1 = ["milk", "bread", "eggs", "bread", "butter"]
customer2 = ["bread", "butter", "cheese", "milk"]

# First Convert to sets to remove duplicates within each customer
customer1 = set(customer1)


customer2 = set(customer2)


# 1) unique items bought by both customers
 
print(customer1.symmetric_difference(customer2))

# 2) common items bought by both customers
print(customer1.intersection(customer2))


# 3) Display the total number of unique items purchased across both customers
print(len(customer1.union(customer2)))







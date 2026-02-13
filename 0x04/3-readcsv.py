#!/usr/bin/python3
# a module that reads the content in a csv file

import csv

with open("data.csv") as csvfile: # open the csv file
    csvreader = csv.reader(csvfile, delimiter=",") # read the file using csv reader
    for row in csvreader: # iterate through each row
        print(" ".join(row)) # print the row as a string


#!/usr/bin/python3
# a module that reads the content in a csv file

import csv

with open("data.csv") as csvfile: # open the csv file
    csvreader = csv.reader(csvfile, delimiter=",") # read the file using csv reader
    for row in csvreader: # iterate through each row
        print(" ".join(row)) # print the row as a string

from collections import defaultdict
from typing import Dict, List

with open("students.txt", "r", encoding = "utf-8") as file:
    student_data: Dict[str, List[str]] = defaultdict(list)
    for line in file:
        A, name = line.strip().split(",")
        student_data[A].append(name)
        print(student_data)
        
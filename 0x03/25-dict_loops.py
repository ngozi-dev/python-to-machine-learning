#!/usr/bin/python3
# a module that displays studens and their scores


# Given dictionary of students and their scores
scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

# Task 1: Print all students who scored above 80
above_80 = []  #Initialize an empty list called above_80 to store names with scores above 80.
for name, score in scores.items():
    if score > 80:
        above_80.append(name)

print("Students scoring above 80:", above_80)

# Task 2: Find and print the student with the highest score
best_student = None  #Initialize best_student as None and best_score as -infinity (or a very small number).
best_score = -1

for name, score in scores.items():
    if score > best_score:  #If score > best_score, set best_student to name and best_score to score.
        best_student = name
        best_score = score

print("Highest scoring student:", best_student, "with score", best_score)
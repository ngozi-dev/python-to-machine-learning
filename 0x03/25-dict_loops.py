#!/usr/bin/python3
# a module that displays studens and their scores

candidates = {
    "students": ["Alice", "Bob", "Charlie", "Diana"],
    "scores": [85, 90, 78, 92],
}

print(candidates)

for student, score in scores.item():
    if score > 80:
        print(f"{student}:{score}")

# 24-dict_loop.py

# Create a dictionary of students and their scores
scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

# 1) Print all students who scored above 80
print("Students who scored above 80:")
for student, score in scores.items():
    if score > 80:
        print(f"{student}: {score}")

# 2) Find and print the student with the highest score
# Using max with a key function to get the key (student) with the maximum score value
top_student = max(scores, key=lambda s: scores[s])
top_score = scores[top_student]

print("\nTop student:")
print(f"{top_student} with a score of {top_score}")


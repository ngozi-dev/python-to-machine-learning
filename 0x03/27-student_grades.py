#!/usr/bin/python3
# a module that displays students and their scores

# given set
students = ["Alice", "Bob", "Charlie"]

grades = dict()

# input three scores for each student
students = {
    "Alice": [80, 90, 85],
    "Bob": [70, 60, 75],
    "Charlie": [95,88,92]
}

# store them in a list
students = ["Alice", "Bob", "Charlie"]
scores = [80, 90, 85, 70, 60, 75, 95, 88, 92]

# calculate average score of each student
average_scores = [80 & 80 & 85]//100
print(average_scores) 



# 24-dict_grades_manager.py

# 2. Create a list of 3 students
students = ["Alice", "Bob", "Charlie"]

# 3. Create an empty dictionary called grades
grades = {}

# 4. For each student, ask the user to enter 3 scores (numbers)
for student in students:
    scores = []
    print(f"Enter 3 scores for {student}:")
    for i in range(1, 4):
        while True:
            try:
                value = float(input(f"  Score {i}: "))
                scores.append(value)
                break
            except ValueError:
                print("    Please enter a valid number.")
    # Store in the dictionary: key is the student's name, value is the list of scores
    grades[student] = scores

# 5. After input, calculate the average score for each student
averages = {}
for student, scores in grades.items():
    averages[student] = sum(scores) / len(scores)

# Print each student’s name with their average score
print("\nAverages per student:")
for student, avg in averages.items():
    print(f"{student}: {avg:.2f}")

# 6. Find and print the student with the highest average score
top_student = max(averages, key=averages.get)
top_score = averages[top_student]

print("\nTop student:")
print(f"{top_student} with an average score of {top_score:.2f}")
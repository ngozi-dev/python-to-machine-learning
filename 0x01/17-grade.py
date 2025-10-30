#!/usr/bin/python3
# a module that grades students based on their scores

def grade(Score):
    if 90 <= Score <= 100:
        return "A"
    elif 80 <= Score < 90:
        return "B"
    elif 70 <= Score < 80:
        return "C"
    elif 60 <= Score < 70:
        return "D"
    elif Score >= 0 and Score < 60:
        return "F"
    else:
        return "Invalid score"


if __name__ == "__main__":
    score = float(input("Enter student score: "))
    print("Grade:", grade(score))

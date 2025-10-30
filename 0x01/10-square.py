#!/urs/bin/python
# a module that calculates the area of a square


def square(side):
    return side ** 2


side = float(input("Enter the side of the square:"))
area = square(side)
print("The area of the square is: {:.2f}".format(area))


#!/usr/bin/python3
# a module that reads a txt file

# Create a file called books.txt
# Each line should contain book title, author, and year 
# separated by a semicolon (e.g., The Hobbit;J.R.R. Tolkien;1937).
# Write a function that reads the file and stores the data in a 
# dictionary where the key is the author and the value is a list of their books (title and year).

def read_books_file(filename):
    books_by_author = {}
    with open(filename, "r") as file:
        for line in file.readlines():
            clean_line = line.strip()
            if not clean_line:
                continue
            else:
                author,title,year_str = clean_line.split(";")
                year = int(year_str)
                if author not in books_by_author:
                    books_by_author[author] = []
                    books_by_author[author].append((title,year))
                else:
                    books_by_author[author].append((title,year))
    return books_by_author

if __name__ == "__main__":
  result =  read_books_file("books.txt")
  print(result)                    
'''
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
'''

class Library:
    def __init__(self,no_of_books, books):
        self.no_of_books = no_of_books
        self.book = books
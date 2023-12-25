# Library

# Write a class structure that implements a library. Classes:

# 1) Library - name, books = [], authors = []

# 2) Book - name, year, author (author must be an instance of Author class)

# 3) Author - name, country, birthday, books = []

# Library class

# Methods:

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

# - group_by_author(author: Author) - returns a list of all books grouped by the specified author

# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds the amount of all existing books



 

class Author:
    def __init__(self, name, country, birthday) :
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    
    # def write(self, book_name, year):
    #     book = Book(book_name, year)
    #     self.books.append(book)
    #     Book.books_exist += 1
    def __list__(self):
        author_list = [self.name, self.country, self.birthday]
        return author_list
        
    
    def __repr__(self):
        for i in self.books:
            print(f"We have a book named {i.__list__()[0]} dated {i.__list__()[1]}")


class Book:
    books_exist = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
    
    def __list__(self):
        book = [self.name, self.year, self.author]
        return book
    
    def __repr__(self):
        print(f"This book called {self.name}, it was written in {self.year} by author named {self.author.__list__()}")
        
class Library:
    labrary_books = 0
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    
    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        Book.books_exist += 1
        Library.labrary_books +=1
        if author not in self.authors:
            self.authors.append(author)
        else:
            pass
    
    def group_by_author(self, author: Author):
        if author in self.authors:
            for i in self.books:
                if author in i.__list__():
                    print(f"This author has the book called {i.__list__()[0]}")
                else:
                    pass
        else:
            print("No such author in labrary")
    
    def group_by_year(self, year: int):
        coincedence = 0
        for i in self.books:
            if year in i.__list__():
                print(f"We have a book called {i.__list__()[0]}.")
                coincedence = 1
            elif year not in i.__list__():
                pass
        if coincedence == 0:
            print("We have no books from this year")
    
    def __repr__(self):
        print(f"We have {Library.labrary_books} in our library.")
        print("We have such authors as: ")
        for i in self.authors:
            print(i.__list__()[0])
        print("Also we have such books as: ")
        for i in self.books:
            print(i.__list__()[0])
    

my_author = Author("John Smith", "France", 1960)
your_author = Author("Will Smith", "France", 1963)


my_library = Library("St.Harbor")
my_library.new_book("Sinister", 1996, my_author)
my_library.new_book("Simphony", 1996, my_author)
my_library.new_book("Tojy", 1995, my_author)
my_library.new_book("Lalaland", 1995, your_author)

my_library.group_by_author(my_author)
my_library.group_by_author(your_author)

my_library.group_by_year(1996)

my_library.__repr__()


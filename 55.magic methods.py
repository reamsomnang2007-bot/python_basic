# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's buil-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found!"
       
    
book1 = Book("Atomic Habbits", "Jame Clear", 320)
book2 = Book("The Habbit", "J.R.R Tolkien", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

print(book3)
print(book1 == book3)
print(book2 < book3)
print(book1 > book2)
print(book2 + book1)
print("Habbit" in book2)
print(book1["title"])



    

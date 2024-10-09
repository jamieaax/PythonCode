class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    #use __eq__
    def __eq__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    #use __ge__ 
    def __ge__(self, value):
         if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
         return self.price >= value.price

    #use __it__
    def __lt__(self, value):
         if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
         return self.price < value.price
    

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the eye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

#print(b1 == b3)

#In Python with comparisons of objects
#It's compared with memory location and not with common attributes

#with methods like __eq__() __ge__() and __lt__()
#We can compare our objects through attributes

#without these methods print(b1 == b3) would output as false
#this is because they are different objects in memory


#print(b1 == b2)
#print(b1 == 42)

#print(b2 >= b1)
#print(b2 < b1)

books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books])
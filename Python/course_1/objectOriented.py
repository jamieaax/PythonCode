#class - blueprint for creating objects
#method - regular functions apart of a class
#attribute - variables that hold data
#object - specific instance of class
#inheritance
#composition

#create basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    #create instance methods
    def getprice(self):
        if hasattr(self, "_discount"): #checks if attribute is present
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount

#create instance
book1 = Book("Brave new world", "Leo Tolstoy", 1225, 39.95)
book2 = Book("War and Peace", "JD salinger", 243, 39.95)

#print price of book1
print(book1.getprice())

print(book2.getprice())
book2.setdiscount(0.25)
print(book2.getprice())

#properties with double underscores are hidden
print(book2._Book__secret)

#print class and property
#print(book1)
#print(book1.title)
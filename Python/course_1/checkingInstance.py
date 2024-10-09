class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("The catcher in the rye")
b2 = Book("Hunger Games")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The Sun")

#print(type(b1))
#print(type(n1))

#compare two types togrther
#print(type(b1) == type(b2))
#print(type(b1) == type(n2))

#use isInstance to compare specific instances to a known type
print(isinstance(b1,Book))
print(isinstance(n1,Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2,object))
#n2 is an instance of the object class


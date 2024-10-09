#magic method
#customise object behaviour
#control access to attribute values
#build in comparison and equality testing capabilities
#allow objects to be called like functions

class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

   #use __str__ to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
   #use __repr__ to return an object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"
    

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the eye", "JD Salinger", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))

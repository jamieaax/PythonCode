from dataclasses import dataclass

@dataclass
class Book: 
   title: str
   author: str
   pages: int
   price: float

   # __post_init__ lets us customise additional properties
   #after the object has been initialised via built-in __init__
   def __post_init__(self):
      self.description = f"{self.title} by {self.author}, {self.pages} pages"



#created instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the rye", "JD Salinger", 234, 29.95)

#use the description attribute
print(b1.description)
print(b2.description)
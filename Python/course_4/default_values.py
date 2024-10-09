from dataclasses import dataclass, field

import random

def price_func():
   return float(random.randrange(20,40))

@dataclass
class Book: 
   #class' defined default values
   title: str = "No Title"
   author: str = "No Author"
   pages: int = 0
   price: float = field(default_factory=price_func)
   #price: float = field(default=10.0)

   #if an attribute doesnt have a default value
   #it must come first in the class

#b1 = Book()
#print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the rye", "JD Salinger", 234)
print(b2)
print(b3)

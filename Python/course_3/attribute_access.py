from typing import Any


class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, cost {self.price}"
    
    #use __getattribute__ when an attr is retrieved
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)


    #use __setattr__ when an attribute value is set
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)
    
    #use __getattr__ when __getattribute__ lookup fails
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the eye", "JD Salinger", 29.95)

b1.price = float(40)
print(b1.randomprop)
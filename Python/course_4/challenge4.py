#convert classes into dataclasses
#subclasses required to override the magic method that makes them sortable

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Asset(ABC): #ABC makes the class non-instanitable 
    #price: float

    @abstractmethod #Child classes must inherit its parent abstract method with the correct arguments
    def __lt__(self, other):
        pass



@dataclass
class Stock(Asset):
    ticker: str
    price: float
    company: str
    
    def __lt__(self, other):
        return self.price < other.price
    

@dataclass
class Bond(Asset):
    price: float
    description: str
    duration: int
    yieldamt: float

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt



stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 135.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 year US treasury", 30, 4.38),
    Bond(96.70, "10 year US treasury", 10, 4.28),
    Bond(98.65, "5 year US treasury", 5, 4.43),
    Bond(99.57, "2 year US treasury", 2, 4.98)
]

try:
    ast = Asset(100.0)
except:
    print("Can't instaniate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("----------")
for bond in bonds:
    print(bond)
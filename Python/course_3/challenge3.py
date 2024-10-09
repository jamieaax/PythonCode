#use a magic method to make stocks and bonds sortable
#stocks should sort from low to high on price
#bonds should sort from low to high on yield


from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        pass



class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def __str__(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
    def __lt__(self, other):
        return self.price < other.price

        
class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt

    def __str__(self):
        return f"{self.description}: {self.duration}yr: ${self.price}: {self.yieldamt}%"

    def __lt__(self, other):
        self.yieldamt < other.yieldamt

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

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("----------")
for bond in bonds:
    print(bond)
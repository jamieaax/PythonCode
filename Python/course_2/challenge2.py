#create a class structure to represent stocks and bonds

#requirement:
#-- both stocks and prices have a price
#-- stocks have a company name and ticker
#-- bonds have a description, duration and yield
#-- you should not be able to instaniate the base class
#-- subclasses are required to override get_description()
#-- get_description() returns formars for stocks and bonds
# for stocks: "Ticker: Company -- $price"
# for bonds: "description: duration'yr' : $price : yieldamt%"

from abc import ABC, abstractmethod

class Asset():
    def __init__(self, price):
        self.price = price
        

    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"

class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt


    def get_description(self):
        return f"{self.description}: {self.duration}yr: ${self.price}: {self.yieldamt}%"


try:
    ast = Asset(100.0)
except:
    print("Can't instantiate Asset!")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

us30yr = Bond(95.31, "30 year US treasury", 30, 4.38)
us10yr = Bond(96.70, "10 year US treasury", 10, 4.28)
us5yr = Bond(98.65, "5 year US treasury", 5, 4.43)
us2yr = Bond(99.57, "2 year US treasury", 2, 4.98)

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())

print(us30yr.get_description())
print(us10yr.get_description())
print(us5yr.get_description())
print(us2yr.get_description())
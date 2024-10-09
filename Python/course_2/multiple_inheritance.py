class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()
        
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)
        #since there's two self.name in the two inherited classes 
        #it will output the class that is defined first from left to right

c = C()
print(C.__mro__) 
# C.__mro__ shows the resolution order of the classes
#basically which class gets defined first
c.showprops()
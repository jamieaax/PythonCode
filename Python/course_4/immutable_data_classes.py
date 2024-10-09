from dataclasses import dataclass

@dataclass(frozen=True) #cannot change anything in the dataclass
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval


obj = ImmutableClass("Another String", 20)
print(obj.value1, obj.value2)

#attempting to change the value of an immutable class throws an exception
#obj.value1 = "Another String"
#print(obj.value1)

#even functions within the class can't change anything
obj.some_func(20)
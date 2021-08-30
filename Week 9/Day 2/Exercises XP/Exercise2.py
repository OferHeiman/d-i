class Currency:
    def __init__(self,name,amount) -> None:
        self.name = name
        self.amount = amount
    

    def __str__(self):
        return f"{self.amount} {self.name}"
    

    def __int__(self):
        return self.amount

    
    def __repr__(self):
        return f"{self.__class__.__name__} : {self.amount} {self.name}"
    

    def __add__(self,other):
        try:
            return self.amount+other
        except:
            if other.name == self.name:
                return self.amount+other.amount
            else:
                return f"TypeError: Cannot add between Currency type {self.name} and {other.name}"
    
    def __iadd__(self,other):
        try:
            self.amount += other
            return self
        except:
            if other.name == self.name:
                self.amount+=other.amount
                return self
            else:
                return f"TypeError: Cannot add between Currency type {self.name} and {other.name}"

    def __call__(self):
        return self.amount


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1+=5
print(c1)
c1 += c2
print(c1)
print(c1+c3)
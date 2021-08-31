class Circle():
    def __init__(self,name,**kwargs):
        self.name = name
        try:
            self.radius = kwargs['radius']
        except:
            self.diameter = kwargs['diameter']
    
    def area(self):
        try:
            return self.radius**2*3.14
        except:
            return (self.diameter/2)**2*3.14
    
    def __repr__(self) -> str:
        try:
            return f"I am a {self.__class__.__name__},my radius is {self.radius}, and my area is {self.area()}"
        except:
            return f"I am a {self.__class__.__name__},my diameter is {self.diameter}, and my area is {self.area()}"
    
    def __add__(self,other):
        try:
            return self.radius+other.radius
        except:
            return self.diameter+other.diameter
            
    
    def __eq__(self, other):
        try:
            if self.radius == other.radius:
                return "The Circles are equal"
            elif self.radius > other.radius:
               return f"{self.name}is bigger than {other.name}"
            else:
                return f"{other.name} is bigger than {self.name}"
        except:
            if self.diameter == other.diameter:
              return "The Circles are equal"
            elif self.diameter > other.diameter:
               return f"{self.name}is bigger than {other.name}"
            else:
                return f"{other.name} is bigger than {self.name}"
    
    def __lt__(self, other):
        try:
            return self.radius < other.radius
        except:
            return self.diameter < other.diameter


circle1 = Circle('circle1',radius=5)
circle2 = Circle('circle2',radius=10)
print(circle1.area())
print(circle1)
print(circle1+circle2)
print(circle1 == circle2)
circles_list = [circle2.name,circle1.name]
print(circles_list)
print(sorted(circles_list))
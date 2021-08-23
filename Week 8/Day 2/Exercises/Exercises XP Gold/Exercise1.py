class Circle():
    def __init__(self,radius = 1.0):
        self.radius = radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def printDefinitions(self):
        print(f"The perimeter of the circle is: {self.perimeter()} and the area of the circle is: {self.area()}")

circle = Circle(5)
circle.printDefinitions()
import math




class Temperature:
    def __init__(self,temperature: int):
        self.temperature = temperature
    
    def change_temperature(self):
        new_temperature = input("Which type of temperature would you like to convert to? ").capitalize()
        if type(self) == Temperature and new_temperature == 'Celsius':
            self.__class__ = Celsius
        elif type(self) == Temperature and new_temperature == 'Kelvin':
            self.__class__ = Kelvin
        elif type(self) == Temperature and new_temperature == 'Fahrenheit':
            self.__class__ = Fahrenheit
        elif type(self) == Celsius and new_temperature == 'Kelvin':
            self.temperature += 273.15
            self.__class__ = Kelvin
        elif type(self) == Celsius and new_temperature == 'Fahrenheit':
            self.temperature = (self.temperature * 1.8) + 32  
            self.__class__ = Fahrenheit
        elif type(self) == Fahrenheit and new_temperature == 'Kelvin':
            self.temperature = 273.5 + ((self.temperature - 32.0) * (5.0/9.0))
            self.__class__ = Kelvin
        elif type(self) == Fahrenheit and new_temperature == 'Celsius':
            self.temperature = (self.temperature - 32)/1.8 
            self.__class__ = Celsius
        elif type(self) == Kelvin and new_temperature == 'Fahrenheit':
            self.temperature = math.floor(((self.temperature-273.15)*1.8) + 32)
            self.__class__ = Fahrenheit
        elif type(self) == Kelvin and new_temperature == 'Celsius':
            self.temperature -= 273.15
            self.__class__ = Celsius
        elif type(self) == Kelvin and new_temperature == 'Temperature':
            self.__class__ = Temperature
        elif type(self) == Celsius and new_temperature == 'Temperature':
            self.__class__ = Temperature
        elif type(self) == Fahrenheit and new_temperature == 'Temperature':
            self.__class__ = Temperature


class Celsius(Temperature):
    def __init__(self, temperature: int):
        super().__init__(temperature)
class Kelvin(Temperature):
    def __init__(self, temperature: int):
        super().__init__(temperature)
class Fahrenheit(Temperature):
    def __init__(self, temperature: int):
        super().__init__(temperature)

test = Celsius(50)
test.change_temperature()
print(f"{test.temperature} {type(test)}")

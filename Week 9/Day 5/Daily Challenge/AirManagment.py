import datetime

class Company:
    def __init__(self,id:str,name:str) -> None:
        self.id = id
        self.name = name
        self.planes = []
    
    def add_planes(self,*args): #add new Airplanes to Company list of planes
        list_of_planes = args
        for plane in list_of_planes:
            self.planes.append(plane)


class Airport:
    def __init__(self,city:str) -> None:
        self.city = city
        self.planes = []
        self.scheduled_departues = []
        self.scheduled_arrivals = []
    
    def schedule_flight(self,destination,datetime):
        pass

    


class Airplane:
    def __init__(self,id:int,current_location:Airport,company:Company) -> None:
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        self.current_location = destination
    
    def location_on_date(self,date):
        pass
    
    # @staticmethod
    # def date_time(flight): #returns the date of flight
    #     return flight.date

    def add_flight(self,flight):  #adds flight to the Airplane list of next flights
        self.next_flights.append(flight)
        self.next_flights.sort(key=lambda flight:flight.date)



class Flight:
    def __init__(self,date:datetime.date,destination:Airport,origin:Airport,plane: Airplane) -> None:
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{self.destination}{plane.company.id}{self.date}"

El_Al = Company("EL","EL AL")
Turkish_Airlines = Company("TA","Turkish Airlines")
Ben_Gurion = Airport("TLV")
Heathrow = Airport("London")
John_F_Kennedy = Airport("NYC")
EL_AL_Plane1 = Airplane(1,Ben_Gurion,El_Al)
EL_AL_Plane2 = Airplane(2,Heathrow,El_Al)
Turkish_Airlines_Plane1 = Airplane(1,Heathrow,Turkish_Airlines)
Turkish_Airlines_Plane2 = Airplane(2,Ben_Gurion,Turkish_Airlines)
El_Al.add_planes(EL_AL_Plane1,EL_AL_Plane2)
Turkish_Airlines.add_planes(Turkish_Airlines_Plane1,Turkish_Airlines_Plane2)
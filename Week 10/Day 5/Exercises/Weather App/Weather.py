from pyowm.owm import OWM
from pyowm.utils import timestamps
owm = OWM('697e2177593a2bfecfc2c4a414d51842')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Tel Aviv,IL')  
city_name = observation.location.name
weather = observation.weather
print(f"City name is: {city_name}")
print(f"The weather is {weather.status},a more detailed weather is {weather.detailed_status}")
print(f"Current wind info: \nwind speed:{weather.wind().get('speed')} \ndeg:{weather.wind().get('deg')}")
print(f"sunrise: {weather.sunrise_time(timeformat='iso')} \nsunset: {weather.sunset_time(timeformat='iso')}")

print("\nNew city:")
user_city = input("City name: ")
user_country = input("Country name: ").upper()
reg = owm.city_id_registry()
list_of_locations = reg.locations_for(user_city, country=user_country)
user_city = list_of_locations[0]
weather = mgr.weather_at_id(user_city.id).weather 
print(f"The weather is {weather.status},a more detailed weather is {weather.detailed_status}")
print(f"Current wind info: \nwind speed:{weather.wind().get('speed')} \ndeg:{weather.wind().get('deg')}")
print(f"sunrise: {weather.sunrise_time(timeformat='iso')} \nsunset: {weather.sunset_time(timeformat='iso')}")
print("Forcast: ")
print(f"Daily Forecast: {mgr.forecast_at_place(user_city.name,'daily').forecast}")
print(f"Forecast in 3 hours: {mgr.forecast_at_place(user_city.name,'3h').forecast}")

print("Air pollution Haifa: ")
mgr = owm.airpollution_manager()
print(f"Latest CO index in {user_city.name}: {mgr.coindex_around_coords(user_city.lat,user_city.lon)}")
print(f"Available CO index in the last 24 hours: {user_city.name}: {mgr.coindex_around_coords(user_city.lat, user_city.lon,start=timestamps.yesterday(), interval='day')}")
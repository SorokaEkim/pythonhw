
import geopy.geocoders
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='tutorial')
location = geolocator.geocode('Cheboksary')

print(location)
print((location.latitude, location.longitude))
print(location.raw)
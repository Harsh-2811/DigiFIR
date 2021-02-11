
"""import requests

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
api_key = 'Sjbs1jct2RbI-1oyW7G9ow6fJBglVWeUaizszl26Q_E' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
data = r.json()

latitude = data['items'][0]['position']['lat']
longitude = data['items'][0]['position']['lng']

print(latitude,longitude)"""
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="digifir")
location = geolocator.reverse("21.2329613, 72.81608609999999")
print(location.address)
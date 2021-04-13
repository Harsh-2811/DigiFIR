
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
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="geoapiExercises")

        # place input by geek
place = "Hirabag"
location = None
def do_geocode(place, attempt=1, max_attempts=5):
    try:
        return geolocator.geocode(place)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return do_geocode(place, attempt=attempt+1)
        raise

location = do_geocode(place)
# traverse the data
data = location.raw
loc_data = data['display_name'].split()

postal = loc_data[-2]
postal = postal[:-1]

print(postal)


"""Process data to and from Google maps"""

import requests

GOOGLE_MAP_API_KEY="AIzaSyApA_At8_2MYDiIwWrlVkvJXY218hXm5wA"


user_lat = 37.785152
user_lon = -122.406581
loc_lat = 37.762028
loc_lon = -122.470790

def gets_min_travel_to_location_from_user_transit(user_lat, user_lon, loc_lat, loc_lon):
    """Gets the time that it'll take a user to get to a location via transit"""

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={0},{1}&destination={2},{3}&departure_time=now&traffic_model=best_guess&mode=transit&key={4}".format(str(user_lat), str(user_lon), str(loc_lat), str(loc_lon), str(GOOGLE_MAP_API_KEY))

    r = requests.get(url)

    adict = r.json()

    if "error_message" not in adict:

        arrival_time_raw = adict['routes'][0]['legs'][0]['duration']['text']
        arrival_time_raw_split = arrival_time_raw.split(":")

    return str(arrival_time_raw_split[0])

def gets_min_travel_to_location_from_user_walk(user_lat, user_lon, loc_lat, loc_lon, transit_mode):
    """Gets the time that it'll take a user to get to a location via transit"""

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={0},{1}&destination={2},{3}&departure_time=now&traffic_model=best_guess&mode={4}&key={5}".format(str(user_lat), str(user_lon), str(loc_lat), str(loc_lon), str(transit_mode), str(GOOGLE_MAP_API_KEY))

    r = requests.get(url)

    adict = r.json()

    if "error_message" not in adict:

        arrival_time_raw = adict['routes'][0]['legs'][0]['duration']['text']
        arrival_time_raw_split = arrival_time_raw.split(":")

    return str(arrival_time_raw_split[0])


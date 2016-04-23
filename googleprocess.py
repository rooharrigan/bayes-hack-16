"""Process data to and from Google maps"""

import os
import requests

GOOGLE_MAP_API_KEY = os.environ.get("GOOGLE_MAP_API_KEY")


def gets_min(user_lat, user_lon, loc_lat, loc_lon, transit_mode):
    """Gets the time that it'll take a user to get to a location via transit"""

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={0},{1}&destination={2},{3}&departure_time=now&traffic_model=best_guess&mode={4}&key={5}".format(str(user_lat), str(user_lon), str(loc_lat), str(loc_lon), str(transit_mode), str(GOOGLE_MAP_API_KEY))

    r = requests.get(url)

    adict = r.json()

    if "error_message" not in adict:

        arrival_time_raw = adict['routes'][0]['legs'][0]['duration']['text']
        arrival_time_raw_split = arrival_time_raw.split(":")

    return str(arrival_time_raw_split[0])


def gets_min_travel_to_location_from_user(user_lat, user_lon, locations):
    """Gets the time that it'll take a user to get to a location via transit and car"""

    new_locations = []

    for location in locations:
        transit = gets_min(user_lat, user_lon, location[2], location[3], "transit")
        car = gets_min(user_lat, user_lon, location[2], location[3], "car")
        info = {"name": location[0], "des": location[1], "lat": location[2], "lng": location[3], "transit": transit, "car": car}
        new_locations.append(info)

    return new_locations

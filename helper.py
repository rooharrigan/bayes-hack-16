import requests
import os


RIDB_API_KEY = os.environ.get("RIDB_API_KEY")

def get_rec_areas(latitude, longitude):
    """Makes an API call to the RIDB."""

    payload = {"apikey": RIDB_API_KEY, "limit":"10", "radius":"50", "latitude": latitude, "longitude": longitude}

    response = requests.get("https://ridb.recreation.gov/api/v1/recareas", params=payload).json()

    rec_areas = []

    for locations in response["RECDATA"]:
        name = locations["RecAreaName"]
        lat = locations["RecAreaLatitude"]
        lon = locations["RecAreaLongitude"]
        description = locations["RecAreaDescription"]
        rec_areas.append((name, description, lat, lon))

    return rec_areas


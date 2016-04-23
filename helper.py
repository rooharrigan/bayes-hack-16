import requests
import os


RIDB_API_KEY = os.environ.get("RIDB_API_KEY")
def get_rec_areas(latitude, longitude):
    """Makes an API call to the RIDB."""


    payload = {"apikey": RIDB_API_KEY, "limit":"10", "radius":"50", "latitude": latitude, "longitude": longitude}

    response = requests.get("https://ridb.recreation.gov/api/v1/recareas", params=payload).json()

    return response

print get_rec_areas("37.804364", "-122.271114")
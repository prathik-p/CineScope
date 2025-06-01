import requests
from django.conf import settings

OMDB_API_URL = "http://www.omdbapi.com/"

def fetch_from_omdb(params):
    # Add the OMDB API key from Django settings to the request parameters
    params['apikey'] = settings.OMDB_API_KEY
    try:
        response = requests.get(OMDB_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            return {"Error": data.get("Error", "Unknown API error"), "Response": "False"}
    except requests.exceptions.RequestException as e:
        return {"Error": str(e), "Response": "False"}
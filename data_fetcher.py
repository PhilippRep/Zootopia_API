import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("Missing API_KEY")
HEADERS = {
    'X-Api-Key': f'{API_KEY}'
}

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = API_URL + animal_name
  response = requests.get(url, headers=HEADERS, timeout=5)
  content = response.json()
  if not content:
      return None
  return content


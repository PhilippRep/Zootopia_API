import requests
from important.config import API_KEY

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
  response = requests.get(animal_name, headers=HEADERS)
  content = response.json()
  return content


"""create a website with specific input from an API"""
import data_fetcher
import animals_web_generator

API_URL = "https://api.api-ninjas.com/v1/animals?name="


def main():
    """controlling of the Programm"""
    which_animal = input("Enter a name of an animal: ")
    url = API_URL + which_animal
    animals_data = data_fetcher.fetch_data(url)
    animals_web_generator.get_information_from_animals(animals_data)
    animals_web_generator.read_html()


if __name__ == "__main__":
    main()

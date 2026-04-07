"""create a website with specific input from an API"""
import data_fetcher
import animals_web_generator


def main():
    """controlling of the Programm"""
    which_animal = input("Enter a name of an animal: ")
    animals_web_generator.get_information_from_animals(which_animal)
    animals_web_generator.read_html()


if __name__ == "__main__":
    main()

from data_fetcher import fetch_data
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

HTML_TEMPLATE_FILE = BASE_DIR / "animals_template.html"
WEBSITE_HTML = BASE_DIR / "animals.html"
OLD_TEXT_IN_HTML = "__REPLACE_ANIMALS_INFO__"

def read_html():
    """read html file"""
    with open(HTML_TEMPLATE_FILE, "r", encoding="utf-8") as file:
        html_content = file.read()
        return html_content

def serialize_animal(animal_obj):
    if animal_obj is None or animal_obj == {}:
        return f"<h2>The animal doesn't exist.</h2>"
    characteristics = animal_obj.get('characteristics', {})
    animal_type = characteristics.get("type")
    diet = characteristics.get("diet")
    lifespan = characteristics.get("lifespan")
    locations = animal_obj.get("locations", [])
    name = animal_obj.get("name", 'Unknown animal')
    if locations:
        first_location = locations[0]
    else:
        first_location = "-"
    parts= []
    parts.append('<li class="cards__item">\n')
    parts.append(f'<div class="card__title">{name}</div></br>\n')
    parts.append('<div class ="card__text">')
    parts.append("<ul>")
    if diet:
        parts.append(f"<li><strong>Diet: </strong>{diet}\n")
    if first_location:
        parts.append(f"<li><strong>Location: </strong>{first_location}</li>\n")
    if animal_type:
        parts.append(f"<li><strong>Type: </strong>{animal_type}</li>\n")
    if lifespan:
        parts.append(f"<li><strong>Lifespan: </strong>{lifespan}</li>\n")
    parts.append('</ul></div>')
    parts.append("</li>\n")

    return "\n".join(parts)

def get_information_from_animals(infos):
    """Printed the Information Name, Diet, first location and typ from every animal.
    If no location is found, it will print nothing
    """
    output = ""
    data= fetch_data(infos)
    if not data:
        output = f"<h2>The animal '{infos}' doesn't exist.</h2>"
    else:
        for animal in data:
            output += serialize_animal(animal)

    new_content = read_html().replace(OLD_TEXT_IN_HTML, output)
    create_new_html_file(new_content)

def create_new_html_file(content):
    with open(WEBSITE_HTML, "w", encoding="utf-8") as file:
        file.write(content)
    print()
    print(f"Website was successfully generated to the file {WEBSITE_HTML}")


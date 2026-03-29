import data_fetcher

HTML_TEMPLATE_FILE = "animals_template.html"
WEBSITE_HTML = "animals.html"
OLD_TEXT_IN_HTML = "__REPLACE_ANIMALS_INFO__"

def read_html():
    """read html file"""
    with open(HTML_TEMPLATE_FILE, "r", encoding="utf-8") as file:
        html_content = file.read()
        return html_content

def serialize_animal(animal_obj):
    if animal_obj == "error":
        return f"<h2>The animal doesn't exist.</h2>"
    characteristics = animal_obj.get('characteristics', {})
    animal_type = characteristics.get("type")
    diet = characteristics.get("diet")
    lifespan = characteristics.get("lifespan")
    locations = animal_obj.get("locations", [])
    if locations:
        first_location = locations[0]
    else:
        first_location = "-"
    output = ""
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div></br>\n'
    output += '<div class ="card__text">'
    output += "<ul>"
    if diet:
        output += f"<li><strong>Diet: </strong>{diet}\n"
    if first_location:
        output += f"<li><strong>Location: </strong>{first_location}</li>\n"
    if animal_type:
        output += f"<li><strong>Type: </strong>{animal_type}</li>\n"
    if lifespan:
        output += f"<li><strong>Lifespan: </strong>{lifespan}</li>\n"
    output += '</ul>'
    output += '</div>'
    output += "</li>\n"

    return output

def get_information_from_animals(infos):
    """Printed the Information Name, Diet, first location and typ from every animal.
    If no location is found, it will print nothing
    """
    output = ""
    for animal in infos:
        output += serialize_animal(animal)

    new_content = read_html().replace(OLD_TEXT_IN_HTML, output)
    create_new_html_file(new_content)

def create_new_html_file(content):
    with open(WEBSITE_HTML, "w", encoding="utf-8") as file:
        file.write(content)
    print()
    print(f"Website was successfully generated to the file {WEBSITE_HTML}")


import swapi


def get_person(id):
    return swapi.get_person(id)


def get_all(resource):
    return swapi.get_all(resource)


def get_residents_by_planet(planet_name):
    planets = get_all('planets')
    for i in planets:
        if i == planet_name:
            return i.get_residents()
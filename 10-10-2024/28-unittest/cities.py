def call_cities(city, country, population=''):
    if population:
        return f"{city.title()}, {country.title()} - {population} inhabitants."
    else:
        return f"{city.title()}, {country.title()}."

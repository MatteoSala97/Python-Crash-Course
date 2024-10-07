users = {
    "gwash": {
        "first_name": "George",
        "last_name": "Washington",
        "informations": {
            "presidential_years": "1789-1797",
            "party": "None",
            "birth_year": 1732
        }
    },
    "jadam": {
        "first_name": "John",
        "last_name": "Adams",
        "informations": {
            "presidential_years": "1797-1801",
            "party": "Federalist",
            "birth_year": 1735
        }
    },
    "tjeff": {
        "first_name": "Thomas",
        "last_name": "Jefferson",
        "informations": {
            "presidential_years": "1801-1809",
            "party": "Democratic-Republican",
            "birth_year": 1743
        }
    }
}

def print_user_info(users):
    for username, info in users.items():
        full_name = f"{info['first_name']} {info['last_name']}"
        presidential_years = info['informations']['presidential_years']
        party = info['informations']['party']
        birth_year = info['informations']['birth_year']
        
        print(f"\nUsername: {username}\nAll the informations about: {full_name}. "
              f"Presidential years: {presidential_years}, Party: {party}, Birth year: {birth_year}")

print_user_info(users)
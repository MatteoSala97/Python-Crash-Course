def create_user(username, first_name, last_name):
    user = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name
    }
    return user

def create_table(material, leg_count, height, length):
    table = {
        'material': material,
        'leg_count': leg_count,
        'height': height,
        'length': length
    }
    return table

def travel_log(city, date, transport):
    travel_entry = {
        'city': city,
        'date': date,
        'transport': transport
    }
    return travel_entry

# user = create_user('johndoe', 'John', 'Doe')
# table = create_table('legno', 4, 1200)
# trip = travel_log('Roma', '2023-05-10', 'aereo')

# print(user)
# print(table)
# print(trip)
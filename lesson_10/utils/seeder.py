from models.workers import Person, Location


location_obj = Location(street='Kreschatik', city='Kyiv')
person_dict = {
    'first_name': 'John',
    'surname': 'Lehnon',
    'age': 40,
    'experience': 20,
    'location': location_obj
}

Person(**person_dict).save()
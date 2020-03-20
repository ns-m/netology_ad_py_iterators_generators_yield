import json


class DataRead:

    countries = []
    with open('../data/countries.json', 'r') as f:
        raw_data = json.load(f)
    for data in raw_data:
        countries.append(data['name']['common'])

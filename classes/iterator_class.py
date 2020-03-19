import requests
import json
from pprint import pprint


class Iterator:
    with open('../data/countries.json', 'r') as f:
        raw_data = json.load(f)
    countrys = []
    for data in raw_data:
        countrys.append(data['name']['common'])
    wiki_url = 'https://en.wikipedia.org/wiki/'
    with open('../data/links.json', 'a') as flink:
        country_links = []
        for country in countrys:
            country_links.append(wiki_url+country)
    print(country_links)

Iterator()
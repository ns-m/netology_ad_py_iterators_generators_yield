import requests
from classes.data_read_class import DataRead
from pprint import pprint


class MyIterator:



    def __init__(self, country_links=[], countries=DataRead()):
        self.session = requests.Session()
        self.countries = countries
        self.country_links = country_links

    def __iter__(self):
        return self

    def __next__(self, country_links, countries):
        wiki_url = 'https://en.wikipedia.org/wiki/'
        # with open('../data/links.json', 'a') as flink:

        for country in countries:
            country_links.append(wiki_url+country)
            print(country)
    print(self.country_links)

MyIterator()
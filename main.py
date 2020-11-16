# importing the requests library
import requests
import json
from types import SimpleNamespace
import pickle

# api-endpoint
URL = "https://pipl.ir/v1/getPerson"

cache = dict()

def get_person_from_server(url):
    r = requests.get(url=URL)
    data = r.json()
    print(data)
    person_details = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
    #print(person_details.person.education.certificate)
    return person_details


def get_person(url):
    if url not in cache:
        cache[url] = get_person_from_server(url)
        return cache[url]

for i in range (1,10):
    x = get_person(URL)




import urllib.request, json 

URL_SOURCE = "https://swapi.dev/api/"

""" with urllib.request.urlopen(URL_SOURCE + 'starships') as url:
    data = json.loads(url.read().decode())
    print(data)

with open('starships.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4) """

# get data from API
with open('people.json') as json_file:
    data = json.load(json_file)
    for p in data['results']:
        with urllib.request.urlopen(p['homeworld']) as url:
            planet = json.loads(url.read().decode())
        print(p['name'] + ' ' + p['gender'] + ' ' + planet['name'])
        
        for i in p['starships']:
            with urllib.request.urlopen(i) as url:
                starship = json.loads(url.read().decode())
                print(starship['name'])

""" # get data from pre-downloaded json
with open('people.json') as json_file:
    data = json.load(json_file)
    for p in data['results']:
        print(p['name'] + ' ' + p['gender'])
        with open('planets.json') as json_file:
            planet = json.load(json_file)
            print(planet['results'][0]['name'])
        for i in p['starships']:
            with open('starships.json') as json_file:
                starship = json.load(json_file)
                print(starship['name'])  """            
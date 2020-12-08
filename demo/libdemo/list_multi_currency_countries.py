import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print('Sorry! Could not get country details!')
    exit()

countries = resp.json()

for country in filter(lambda c: len(c['currencies']) > 1, countries):
    print(f"{country['name']:50} {country['currencies']}")

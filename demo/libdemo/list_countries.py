import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print('Sorry! Could not get country details!')
    exit()

countries = resp.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{country['name']:55} {country['population']:10}")

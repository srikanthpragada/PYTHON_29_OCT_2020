import requests

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code != 200:
    print('Sorry! Country code not found!')
    exit()

details = resp.json()  # Convert JSON to DICT
for name, value in details.items():
    print(f"{name:20} {value}")

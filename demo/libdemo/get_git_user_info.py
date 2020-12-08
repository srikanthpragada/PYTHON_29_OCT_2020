import requests

user = input("Enter GIT username :")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

details = resp.json()   # Convert JSON to DICT

for name,value in details.items():
    print(f"{name:20} {value}")


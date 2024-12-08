# Katie Hilliard, 12/07/2024, Module 9.2 Assignment

import requests

# Test connection
response = requests.get('http://api.open-notify.org/astros.json')
print("Connection test status code:", response.status_code)

# Retrieve and format data
if response.status_code == 200:
    data = response.json()
    print("\nCurrent astronauts in space:")
    for person in data ['people']:
        print(f"- {person['name']} on {person['craft']}")
else:
    print("Failed to retrieve data.")

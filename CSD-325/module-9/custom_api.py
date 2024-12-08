# Katie Hilliard, 12/07/2024, Module 9.2 Assignment

import requests

# Test connection
api_url = "https://anapioficeandfire.com/api/characters/583"
response = requests.get(api_url)
print("Connection test status code:", response.status_code)

# Print response without formatting
print("\nRaw response:")
print(response.text)

# Print response with sae formatting as tutorial
if response.status_code == 200:
    data = response.json()

    # Display formatted data
    print("\nFormatted response:")
    print(f"Name: {data.get('name', 'Unknown')}")
    print(f"Gender: {data.get('gender', 'Unkmown')}")
    print(f"Culture: {data.get('culture', 'Unknown')}")
    print("Born: {data.get('born', 'Unknown')}")
    print(f"Titles: {', '.join(data.get('titles', [])) if data.get('titles') else 'None'}")
    print(f"Aliases: {', '.join(data.get('aliases', [])) if data.get('aliases') else 'None'}")
    print(f"Played By: {', '.join(data.get('playedBy', [])) if data.get('playedBy') else 'Unknown'}")
    print(f"TV Series: {', '.join(data.get('tvSeries', [])) if data.get('tvSeries') else 'None'}")
else:
    print("Failed to retrieve data.")

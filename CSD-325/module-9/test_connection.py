# Katie Hilliard, Module 9.2 Assignment, 12/08/2024

import requests

# Test connection to Google
response = requests.get('http://www.google.com')

# Print status code
print("Connection test status code:", response.status_code)
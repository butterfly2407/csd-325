# Katie Hilliard, 12/1/2024, Module 7.2 Assignment
# Purpose: Define a function that formats city, country, population and languages.

def city_country(city, country, population=None, language=None):
    if population is None:
        population = "Unknown"
    if language:
        return f"{city}, {country} - population {population}, {language}"
    return f"{city}, {country} - population {population}"
    

# Call function with three different values
print(city_country("Tokyo", "Japan"))
print(city_country("South Carolina", "USA", 620000))
print(city_country("Paris", "France", 680000, "French"))












                       


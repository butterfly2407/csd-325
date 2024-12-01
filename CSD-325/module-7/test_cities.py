# Katie Hilliard, 12/1/2024, Module 7.2 Assignment
# Purpose: Test city_country function from city_functions.py

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        # Test with only city and country
        result = city_country("Tokyo", "Japan")
        self.assertEqual(result, "Tokyo, Japan - population Unknown")

    def test_city_country_with_population(self):
        # Test with city, country, and population
        result = city_country("Tokyo", "Japan", population=700000)
        self.assertEqual(result, "Tokyo, Japan - population 700000")

    def test_city_country_with_population_and_language(self):
        # Test with city, country, population, and language
        result = city_country("Tokyo", "Japan", population=700000, language="Japanese")
        self.assertEqual(result, "Tokyo, Japan - population 700000, Japanese")

if __name__ == "__main__":
    unittest.main()



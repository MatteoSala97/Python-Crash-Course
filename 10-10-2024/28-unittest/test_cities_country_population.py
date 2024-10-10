#this file tests `cities.py` to see if the outcome is printed as expected
import unittest
from cities import call_cities 

class CityCountryPopulationTestCase(unittest.TestCase):
    
    def test_city_country_population(self):
        formatted_country  = call_cities('roma', 'italia', '30000000000000')
        self.assertEqual(formatted_country, 'Roma, Italia - 30000000000000 inhabitants.')
        
unittest.main()
#this file tests `cities.py` to see if the outcome is printed as expected
import unittest
from cities import call_cities 

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_country  = call_cities('roma', 'italia')
        self.assertEqual(formatted_country, 'Roma, Italia.')
        
unittest.main()
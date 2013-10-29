#!/usr/bin/env python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        # Anna koukne na index.php
        driver.get("http://www.php")

        man_of_cars = [u'ALFA ROMEO', u'AUDI', u'AUSTIN', u'AUTOBIANCHI', u'BMW',
                       u'CITROEN', u'DACIA', u'DAEWOO', u'DAIHATSU',
                       u'FIAT', u'FORD', u'HONDA', u'HYUNDAI',
                       u'CHRYSLER', u'INNOCENTI', u'KIA', u'LADA',
                       u'LANCIA', u'LAND ROVER', u'MASERATI', u'MAZDA',
                       u'MERCEDES', u'MINI', u'MITSUBISHI', u'NISSAN',
                       u'OPEL', u'PEUGEOT', u'PIAGGIO', u'RENAULT',
                       u'ROVER', u'SAAB', u'SEAT', u'SKODA',
                       u'SMART', u'SUBARU', u'SUZUKI', u'TALBOT',
                       u'TOYOTA', u'VOLKSWAGEN', u'VOLVO', u'ZASTAVA']

        # self.assertIn("Python", driver.title)
        # Zjisti, ze tam jsou vyrobci aut a vybere kazdy z nich

        for man in man_of_cars:
            print 'Calling ' + str(man) + ' ...'
            driver.implicitly_wait(2)
            elem = driver.find_elements_by_tag_name("option")
            for option in elem:
                try:
                    if option.text not in man_of_cars and 'specifikaci' not in option.text:
                        print option.text
                        continue
                except:
                    break
            for option in elem:
                try:
                    if option.text == man:
                        print '... ' + str(option.text) + ' as a response!'
                        driver.implicitly_wait(2)
                        option.click()
                        driver.implicitly_wait(2)
                except:
                    break
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


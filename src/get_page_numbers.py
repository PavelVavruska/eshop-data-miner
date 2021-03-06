#!/usr/bin/env python
# coding=UTF-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secret


class EshopDataMiner(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_website(self):
        driver = self.driver
        # Eržika se podívá na index.php a prolistuje každou stránku
        for number in xrange(1, 3):
            driver.get("http://www.***.cz/e-shop/index.php?strana=%s" % str(number))
            elem_all = driver.find_elements_by_link_text(u"Detail , ceny a objednávání zde ...")
            # na jednotlivé stránce navštíví každou URL adresu celků
            urls = []
            # uloží si odkazy celků, které bude navštěhovat
            for url_object in elem_all:
                url = str(url_object.get_attribute("href"))
                urls.append(url)
            # odkazy na celky navštíví a zjistí si odkazy na součásti
            for url_link in urls:
                driver.get(url_link)
                # uloží všechny informace ze stránky celku
                """
                <tr><td>Značka:</td><td>ALFA ROMEO</td></tr>
                <tr><td>Model:</td><td>Alfa145</td></tr>
                <tr><td>Verze:</td><td>1.4ie / 1351ccm</td></tr>
                <tr><td>Výkon:</td><td>66 kw / 90 HP</td></tr>
                <tr><td>Rok:</td><td>1994/01/01 - 1996/01/12</td></tr>
                <tr><td>Typ:</td><td>930A3</td></tr>
                <tr><td>Motor:</td><td>AR33501</td></tr>
                <tr><td>Katalyzátor:</td><td>Ano</td></tr>
                <img src="obrazky_sys/C010031.gif" id="obrsys" alt="Výfukový systém,výfuk,výfuky,montážní díly... "/>
                <table border="1" id="tabdata" width="590">
                <tr><th>Výfuk</th><th colspan="3">Příslušenství</th></tr>
                <tr><th>Objednací číslo</th><th>Popis príslušenství</th><th>Obj.č MTS</th><th>Obj.č Tyll</th></tr>
                """
                table = driver.find_elements_by_css_selector(".sl2")

                info_model = {'Značka': table.find_element_by_xpath(".//tr[1]/td[2]").text,
                              'Model': table.find_element_by_xpath(".//tr[2]/td[2]").text,
                              'Verze': table.find_element_by_xpath(".//tr[3]/td[2]").text,
                              'Výkon': table.find_element_by_xpath(".//tr[4]/td[2]").text,
                              'Rok': table.find_element_by_xpath(".//tr[5]/td[2]").text,
                              'Typ': table.find_element_by_xpath(".//tr[6]/td[2]").text,
                              'Motor': table.find_element_by_xpath(".//tr[7]/td[2]").text,
                              'Katalyzátor': table.find_element_by_xpath(".//tr[8]/td[2]").text,}

    def test_log_in(self):
        driver = self.driver
        driver.get("http://www.***.cz/admin/") # Log in page
        h2_tag = self.driver.find_element_by_tag_name('h2')
        h2_text = u'Přístup do administrativní části systému'
        self.assertEqual(h2_tag.text, h2_text)
        if h2_tag.text == h2_text:
            driver.find_element_by_name('login').send_keys(secret.get_login())
            driver.find_element_by_name('passw').send_keys(secret.get_pwd())
            driver.find_element_by_name('submit_btn').click()

    def test_website_interaction(self):
        driver = self.driver
        driver.get("http://www.***.cz/page/")

        if not driver.find_element_by_id("checkb").is_selected():  # Check checkbox - Selenium
            driver.find_element_by_id("checkb").click()

        element = driver.find_element_by_name("item_photo") # File upload - Selenium
        element.send_keys("/home/dev/py/eshop-data-miner/data/img/image.png")

        driver.find_element_by_name('submit_product_detail').click() # Click on element - Selenium

    def test_website_js_interaction(self):
        driver = self.driver
        driver.get("http://www.***.cz/page/")

        script1 = u'window.onload = document.getElementsByName("tinymce")[0].checked=true;'  # JS Check
        name = u'product_name'
        script2 = u'window.onload = document.getElementById("product_name2").value = "%s";' % name

        driver.execute_script(script1)
        driver.execute_script(script2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
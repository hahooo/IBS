import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):

        assert 'Google' in self.drv.title

        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)

        assert 'No results found' not in self.drv.page_source

    # def test_is_first_link_on_search_page(self):

        links_block = self.drv.find_elements_by_css_selector('div.g')
        link = links_block[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")

        assert '//selenide.org/' in href

    # def test_is_first_image_on_search_page(self):

        images_button = self.drv.find_elements_by_xpath('//*[contains(text(), "Images")]')
        href = images_button[0].get_attribute("href")
        self.drv.get(href)

        first_image_element = self.drv.find_elements_by_xpath('//*[@id="islrg"]/div[1]/div[1]')
        html = first_image_element[0].get_attribute('innerHTML')

        assert 'selenide.org' in html

        all_button = self.drv.find_element_by_css_selector('a.NZmxZe')
        href = all_button.get_attribute('href')
        self.drv.get(href)

        links_block = self.drv.find_elements_by_css_selector('div.g')
        link = links_block[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        # print(href)
        assert '//selenide.org/' in href


    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
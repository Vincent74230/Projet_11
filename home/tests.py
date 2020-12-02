"""Simple tests of home and credits"""
from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from pathlib import Path

#Path to Chrome driver, for Selenium
BASE_DIR = Path(__file__).resolve().parent.parent

#Options for chrome testing:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class TestPages(TestCase):
    """Class that contains 2 tests (home page and credits)"""
    def test_home_page(self):
        response = self.client.get(reverse("home:index"))
        self.assertEqual(response.status_code, 200)

    def test_mentions_legales(self):
        response = self.client.get(reverse("home:mentions"))
        self.assertEqual(response.status_code, 200)

class TestProject(StaticLiveServerTestCase):
    """Automated testing of chrome browser display"""
    def setUp(self):
        PATH = str(BASE_DIR / 'webdrivers' / 'chromedriver')
        self.browser = webdriver.Chrome((PATH),options=chrome_options,)
        self.browser.implicitly_wait(50)
        self.browser.maximize_window()

    def test_home_page_is_displayed_with_chrome(self):
        """Make sure chrome displays home page and get the title"""
        self.browser.get(self.live_server_url)
        page_title = self.browser.find_element_by_tag_name('h1').text,
        'DU GRAS, OUI MAIS DE QUALITÉ'
        self.assertEqual(
            page_title[0], 'DU GRAS, OUI MAIS DE QUALITÉ'
            )
        
    def tearDown(self):
        self.browser.close()

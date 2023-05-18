import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGo(unittest.TestCase):

    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_RESULTS = (By.XPATH, "//ol[@class='react-results--main']")
    IMAGES_LINK = (By.XPATH, "//li[@class='zcm__item']")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://duckduckgo.com/")

    def tearDown(self):
        self.driver.quit()


    def test_title(self):
        assert "DuckDuckGo" in self.driver.title

    def test_search_input_displayed_enabled(self):
        assert self.driver.find_element(*self.SEARCH_INPUT).is_displayed()
        assert self.driver.find_element(*self.SEARCH_INPUT).is_enabled()

    def test_search_sending_keys(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)

    def test_search_results_are_displayed(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        assert self.driver.find_element(*self.SEARCH_RESULTS).is_displayed()
        assert "Automation" in self.driver.find_element(*self.SEARCH_RESULTS).text

    def test_verify_images_link_is_displayed(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        assert self.driver.find_element(*self.IMAGES_LINK).is_displayed()

    def test_press_images_link(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        self.driver.find_element(*self.IMAGES_LINK).click()
        assert "QA Automation Engineer" in self.driver.title
        self.driver.back()
        assert "Python at DuckDuckGo" not in self.driver.title

    def test_search_input_clearing(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        assert self.driver.find_element(*self.SEARCH_INPUT).get_attribute("value") == ""


    def test_return_to_home_page(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys("QA Automation Engineer")
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        self.driver.back()
        assert "DuckDuckGo" in self.driver.title

    def test_input_field_is_focused(self):
        assert self.driver.find_element(*self.SEARCH_INPUT) == self.driver.switch_to.active_element







import time
import os

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def click(element):
    element.click()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=45):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=45):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def send_keys(self, locator, key):
        self.find_element(locator).send_keys(key)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_until_displayed(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_until_page_loaded(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def scroll_down(self, times):
        self.wait_until_page_loaded()
        for i in range(times):
            # unable to explain why scroll twice doesn't work. Attempted many variations with many waits.
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

    def take_screenshot(self, filename, directory='screenshots'):
        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = os.path.join(directory, filename)

        self.driver.save_screenshot(filepath)

    def click_if_exists(self, locator, time=5):
        try:
            element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
            element.click()
            return True
        except NoSuchElementException:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False



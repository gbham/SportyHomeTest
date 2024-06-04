from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    cookie_info = (By.XPATH, "//*[text()=\"Close\"]")
    # the 'Accept' Cookies and Adverstising Choices is unclickable (manually too) in emulator mode. I assume the desktop version is shown in error?
    # So is the 'Reject' button. But 'Customize' works...?
    cookie_consent = (By.XPATH, "//*[text()=\"Accept\"]")
    # cookie_consent = (By.CSS_SELECTOR, "f\"[class*='{ScCoreButton']\"")

    def handle_cookies_pop_up(self):
        self.wait_until_page_loaded()
        self.click_if_exists(self.cookie_info, 2)
        # self.click_if_exists(self.cookie_consent, 2)
        return self

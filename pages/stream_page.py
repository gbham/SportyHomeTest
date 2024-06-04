from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StreamPage(BasePage):
    viewer_count_label = (By.CSS_SELECTOR, ".ScAnimatedNumber-sc-1iib0w9-0.hERoTc")
    start_watching_button = (By.XPATH, "//*[text()=\"Start Watching\"]")
    video = (By.TAG_NAME, "video")

    def wait_until_loaded(self):
        self.wait_until_page_loaded()
        self.wait_until_displayed(self.video)
        return self

    def check_for_mature_content_popup(self):
        self.click_if_exists(self.start_watching_button)
        return self

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchField(BasePage):
    search_input = (By.CSS_SELECTOR, "input[type=\"search\"]")
    search_btn = (By.CSS_SELECTOR, "button[aria-label=\"Search Button\"]")
    show_search_bar_btn = (By.CSS_SELECTOR, "#__next > div > nav > div.Layout-sc-1xcs6mc-0.hSqeuh > a")

    def click_show_search_bar(self):
        self.click(self.show_search_bar_btn)
        return self

    def enter_search(self, value):
        self.enter_text(self.search_input, value)
        return self

    def perform_search(self):
        self.send_keys(self.search_input, Keys.RETURN)
        return self

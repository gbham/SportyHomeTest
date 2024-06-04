from selenium.webdriver.common.by import By
from pages.base_page import BasePage, click


class SearchResultPage(BasePage):
    stream_image = (By.CLASS_NAME, "tw-image")

    def click_stream(self, num):
        streams = self.find_elements(self.stream_image)
        click(streams[num - 1])

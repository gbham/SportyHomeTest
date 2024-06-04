import pytest
from utils.webdriver_setup import create_mobile_emulator
from pages.search_field import SearchField
from pages.search_result_page import SearchResultPage
from pages.stream_page import StreamPage
from pages.home_page import HomePage


@pytest.fixture(scope="class")
def test_setup(request):
    driver = create_mobile_emulator()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("test_setup")
class TestStream:
    def test_open_stream(self):
        home_page = HomePage(self.driver)
        search_field = SearchField(self.driver)
        search_result_page = SearchResultPage(self.driver)
        stream_page = StreamPage(self.driver)

        self.driver.get("https://twitch.tv/")

        home_page.handle_cookies_pop_up()

        search_field.click_show_search_bar()\
            .enter_search("StarCraft II")\
            .perform_search()

        search_result_page.scroll_down(2)

        search_result_page.click_stream(4)

        stream_page.wait_until_loaded()\
            .check_for_mature_content_popup()\
            .take_screenshot('stream_page.png')

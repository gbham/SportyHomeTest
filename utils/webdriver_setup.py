from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_mobile_emulator(device_name="Pixel 2"):
    chrome_options = Options()
    mobile_emulation = {"deviceName": device_name}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

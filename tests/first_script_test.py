from selenium import webdriver
import allure
import pytest
from base.base_class import Base
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.contacts_page import Contacts_page
from pages.main_page import Main_Page
from pages.tensor_ru_page import Tensor_site


def test_first_scenario(set_up):
    options = webdriver.FirefoxOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    # options.add_argument("--proxy-bypass-list=*")
    # options.add_argument("--start-maximized")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--disable-notifications')
    # options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-infobars")
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    options.set_preference("general.useragent.override",
                                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0")
    options.set_preference("webdriver_assistant.enabled", False)
    options.set_preference("webdriver_accept_untrusted_certs", True)
    options.set_preference("webdriver_enable_native_events", True)
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("browser.cache.offline.enable", False)
    options.set_preference("network.http.use-cache", False)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))


    mp = Main_Page(driver)
    mp.go_to_tensor_banner()

    cp = Contacts_page(driver)
    cp.go_to_site_tensor()

    trp = Tensor_site(driver)
    trp.move_to_more_details()

#@pytest.mark.ran(order=1)
def test_second_scenario():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-infobars")
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0")
    options.set_preference("webdriver_assistant.enabled", False)
    options.set_preference("webdriver_accept_untrusted_certs", True)
    options.set_preference("webdriver_enable_native_events", True)
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("browser.cache.offline.enable", False)
    options.set_preference("network.http.use-cache", False)
    driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

    mp = Main_Page(driver)
    mp.go_to_tensor_banner()

    cp = Contacts_page(driver)
    cp.change_and_check_region()
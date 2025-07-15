from selenium import webdriver
import allure
import pytest
from base.base_class import Base
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.about_company_page import Tensor_about
from pages.contacts_page import Contacts_page
from pages.main_page import Main_Page
from pages.tensor_ru_page import Tensor_site

@allure.description("Первый тест: test_first_scenario")
def test_first_scenario(set_up):
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
    cp.go_to_site_tensor()

    trp = Tensor_site(driver)
    trp.move_to_more_details()

    acp = Tensor_about(driver)
    acp.check_URL_and_pics()

@allure.description("Второй тест: test_second_scenario")
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
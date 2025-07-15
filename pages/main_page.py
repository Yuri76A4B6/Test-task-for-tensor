import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Main_Page(Base):

    url = "https://saby.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    CONTACTS = "//div[@class='sbisru-Header-ContactsMenu js-ContactsMenu']"
    MORE_OFFICES = "//a[@href='/contacts' and @class='sbisru-link sbis_ru-link']"
    LINK_DOWNLOAD_LOCAL_VERSIONS = "//li/a[@href='/download']"

    # GETTERS

    def get_contacts(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CONTACTS)))

    def get_more_offices(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.MORE_OFFICES)))

    def get_link_for_download(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LINK_DOWNLOAD_LOCAL_VERSIONS)))


    # ACTIONS
    def click_contacts(self):
        self.get_contacts().click()
        print("Выполнен клик для перехода в контакты")

    def click_more_offices(self):
        self.get_more_offices().click()
        print("Выполнен клик для выбора других офисов в регионе")

    def click_link_for_download(self):
        self.get_link_for_download().click()
        print("Выполнен клик на элемент 'Скачать локальные версии'")

    def move_to_download_link(self):
        move_to_link = self.get_link_for_download()
        self.driver.execute_script("arguments[0].scrollIntoView();", move_to_link)
        print("Выполнено наведение на элемент 'Скачать локальные версии'")


    # METHODS
    def go_to_tensor_banner(self):
        with allure.step("Go to tensor banner"):
            Logger.add_start_step(method="go_to_tensor_banner")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_contacts()
            self.click_more_offices()
            Logger.add_end_step(url=self.driver.current_url, method="go_to_tensor_banner")

    def go_to_SABY_download(self):
        with allure.step("Go to SABY download"):
            Logger.add_start_step(method="go_to_SABY_download")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.move_to_download_link()
            self.click_link_for_download()
            Logger.add_end_step(url=self.driver.current_url, method="go_to_SABY_download")

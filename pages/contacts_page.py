import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Contacts_page(Base):

    # LOCATORS
    TENSOR_BANNER = "//a[@title='tensor.ru' and @class='sbisru-Contacts__logo-tensor mb-12']"
    LOCATION76 = "(//div/span/span[contains(text(), 'Ярославская обл.')])[1]"
    PARTNER_YAROSLAVL = "//div[@title='Saby - Ярославль']"
    CHANGE_REGION_41_KAMCHATKA = "//li/span/span[contains(text(), '41 Камчатский край')]"
    PARTNER_KAMCHATKA = "//div[@title='Saby - Камчатка']"
    LOCATION41 = "(//div/span/span[contains(text(), 'Камчатский край')])[1]"

    # GETTERS

    def get_tensor_banner(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TENSOR_BANNER)))

    def get_location_76_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LOCATION76)))

    def get_partner_yaroslavl(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.PARTNER_YAROSLAVL)))

    def get_change_region_to_kamchatka(self):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, self.CHANGE_REGION_41_KAMCHATKA)))

    def get_partner_kamchatka(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.PARTNER_KAMCHATKA)))

    def get_location_41_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LOCATION41)))



    # ACTIONS

    def click_tensor_banner(self):
        self.get_tensor_banner().click()
        print("Выполнен клик на баннер 'Тензор'")

    def click_location_76(self):
        self.get_location_76_title().click()
        print("Выполнен клик на Ярославский регион")

    def click_change_region(self):
        self.get_change_region_to_kamchatka().click()
        print("Выполнен клик для перехода на Камчатский край")


    #METHODS
    def go_to_site_tensor(self):
        self.click_tensor_banner()

    def change_and_check_region(self):
        self.click_location_76()
        time.sleep(2)
        self.click_change_region()
        self.check_title_value("камчатский край")
        location_el = self.get_location_41_title()
        self.check_region(location_el, "Камчатский край")
        self.check_info_in_URL()
        check_partner_locator = self.get_partner_kamchatka()
        self.check_info_about_partner(check_partner_locator)




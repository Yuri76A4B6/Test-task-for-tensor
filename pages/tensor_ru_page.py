import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Tensor_site(Base):

    link_for_assert = "https://tensor.ru/about"

    #LOCATORS
    POWER_IN_PEOPLE = "//div/p[contains(text(),'Сила в людях')]"
    MORE_DETAILS = "//p/a[@href='/about']"
    MORE_UNDER_DEVELOPMENT = "//div/a[@href='/about/dev']"

    #GETTERS

    def get_power_in_people(self):
        return WebDriverWait(self.driver, 14).until(EC.visibility_of_element_located((By.XPATH, self.POWER_IN_PEOPLE)))

    def get_more_details(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MORE_DETAILS)))

    def get_more_under(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MORE_UNDER_DEVELOPMENT)))


    def click_more_details(self):
        #action = ActionChains(self.driver)
        move_to_power = self.get_power_in_people()
        self.driver.execute_script("arguments[0].scrollIntoView();", move_to_power)
        #action.move_to_element(move_to_power).perform()
        print("Выполнено наведение на надпись 'Сила в людях'")
        self.get_more_details().click()
        print("Выполнен клик на 'Подробнее'")

    # METHODS

    def move_to_more_details(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        print("Текущий URL:", self.driver.current_url)
        self.click_more_details()

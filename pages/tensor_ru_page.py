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
    POWER_IN_PEOPLE = "//p[@class='tensor_ru-Index__card-title' and contains(text(),'Сила в людях')]"
    MORE_DETAILS = "//p/a[@href='/about']"
    PAUSE_BUTTON = "//div[@class='s-Grid--hide-sm tensor_ru-VideoBanner__button tensor_ru-VideoBanner__button--play']"
    MORE_UNDER_DEVELOPMENT = "//div/a[@href='/about/dev']"

    #GETTERS

    def get_power_in_people(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.POWER_IN_PEOPLE)))

    def get_more_details(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MORE_DETAILS)))

    def get_pause_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.PAUSE_BUTTON)))

    def get_more_under(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MORE_UNDER_DEVELOPMENT)))

    #ACTIONS
    def click_more(self):
        self.get_more_under().click()
        print("Выполнен клик на подробнее тестовый")


    def click_pause(self):
        button = self.get_pause_button()
        self.driver.execute_script("arguments[0].click();", button)
        print("Выполнен клик для остановки видео")

    def click_more_details(self):
        action = ActionChains(self.driver)
        move_to_power = self.get_power_in_people()
        action.move_to_element(move_to_power).perform()
        print("Выполнено наведение на надпись 'Сила в людях'")
        self.get_more_details().click()
        print("Выполнен клик на 'Подробнее'")

    # METHODS

    def move_to_more_details(self):
        self.click_more()
        # self.click_pause()
        # self.scroll_down(0, 700)
        # self.click_more_details()
        # self.assert_url(self.link_for_assert)
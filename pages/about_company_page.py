import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Tensor_about(Base):

    link_for_assert = "https://tensor.ru/about"

    #LOCATORS
    TARGET_RABOTAEM = "//div/h2[contains(text(), 'Работаем')]"
    IMAGE_1 = "(//img[@class='tensor_ru-About__block3-image new_lazy loaded'])[1]"
    IMAGE_2 = "(//img[@class='tensor_ru-About__block3-image new_lazy loaded'])[2]"
    IMAGE_3 = "(//img[@class='tensor_ru-About__block3-image new_lazy loaded'])[3]"
    IMAGE_4 = "(//img[@class='tensor_ru-About__block3-image new_lazy loaded'])[4]"

    #GETTERS

    def get_target_rabotaem(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.TARGET_RABOTAEM)))

    def get_image_1(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.IMAGE_1)))

    def get_image_2(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.IMAGE_2)))

    def get_image_3(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.IMAGE_3)))

    def get_image_4(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.IMAGE_4)))

    # ACTIONS
    def find_target_rabotaem(self):
        move_to_target = self.get_target_rabotaem()
        self.driver.execute_script("arguments[0].scrollIntoView();", move_to_target)
        print("Наведение на надпись 'Работаем'")

    #METHODS

    def check_URL_and_pics(self):
        with allure.step("Check URL and pics"):
            Logger.add_start_step(method="check_URL_and_pics")
            self.assert_url(self.link_for_assert)
            self.find_target_rabotaem()
            time.sleep(5) # Жду загрузки изображений т.к. в пробном тесте размеры были None х None update: проблема была в локаторах
            i1 = self.get_image_1()    # размер изображения через JavaScript можно получить только у элементов "img", а я изначально использовал div
            i2 = self.get_image_2()
            i3 = self.get_image_3()
            i4 = self.get_image_4()
            self.compare_pics_sizes(i1, i2, i3, i4)
            Logger.add_end_step(url=self.driver.current_url, method="check_URL_and_pics")
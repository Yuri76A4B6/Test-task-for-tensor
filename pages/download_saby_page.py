import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Download_Saby_Page(Base):

    # LOCATORS
    LINK_FOR_DOWNLOAD = "//a[@href='https://update.saby.ru/SabyDesktop/master/win32/saby-setup-web.exe']" #Веб-установщик

    #GETTERS

    def get_link_for_download_saby(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LINK_FOR_DOWNLOAD)))

    #ACTIONS

    def click_link_for_download_saby(self):
        with allure.step("Click link for download Saby"):
            Logger.add_start_step(method="click_link_for_download_saby")
            self.get_link_for_download_saby().click()
            print("Выполнен клик для скачивания Веб-установщика")
            time.sleep(20) # щущу ждем, если плохо работают интернеты
            self.check_downloaded_file_size(self.get_link_for_download_saby())
            Logger.add_end_step(url=self.driver.current_url, method="click_link_for_download_saby")
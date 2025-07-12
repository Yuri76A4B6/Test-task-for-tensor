from selenium import webdriver
import allure
import pytest
from base.base_class import Base
from pages.main_page import Main_Page


def test_first_scenario(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    mp = Main_Page(driver)
    mp.go_to_tensor_banner()
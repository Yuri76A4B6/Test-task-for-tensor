class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод для получения URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Метод проверки ппартнера в регионе"""

    def check_info_about_partner(self, locator, expected_result="Saby - Камчатка"):
        value_of_partner = locator.text
        assert value_of_partner == expected_result
        print(f"Название партнера соответствует выбранному региону. Партнер в регионе: {value_of_partner}")

    """Метод проверки региона"""

    def check_region(self, locator, region):
        value_for_check = locator.text
        assert value_for_check == region
        print(f"Успешная проверка региона. Определившийся регион: {value_for_check}")

    """метод проверки Тайтла"""

    def check_title_value(self, value_for_checking):
        title_value = self.driver.title.lower().replace("saby контакты —", "").strip()
        if title_value == value_for_checking:
            print("Title соответствует")
        else:
            print("Регион не совпадает!")
            print(f"Актуальный тайтл страницы: {title_value}")

        # Или можно по-другому (вместо условных операторов)
        # assert title_value == value_for_checking

    """Метод проверки информации о регионе в URL"""

    def check_info_in_URL(self, result = "41-kamchatskij-kraj"): # В данном задании согласно условию выполнения
        get_url = self.driver.current_url              # необходима проверка для камчатского края, поэтому я написал
        get_url_str = str(get_url)                     # аргумент по умолчанию (да, не совсем универсально, каюсь :) )
        if result in get_url_str:
            print("Информация о регионе в URL подтверждена успешно")
        else:
            print("Информация о регионе в URL не подтверждена!")

    """Метод проверки действующей URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Проверка URL прошла успешно. Мы находимся на нужной странице!")

    def compare_pics_sizes(self, image1, image2, image3, image4):
        width1 = self.driver.execute_script("return arguments[0].naturalWidth", image1)
        height1 = self.driver.execute_script("return arguments[0].naturalHeight", image1)
        width2 = self.driver.execute_script("return arguments[0].naturalWidth", image2)
        height2 = self.driver.execute_script("return arguments[0].naturalHeight", image2)
        width3 = self.driver.execute_script("return arguments[0].naturalWidth", image3)
        height3 = self.driver.execute_script("return arguments[0].naturalHeight", image3)
        width4 = self.driver.execute_script("return arguments[0].naturalWidth", image4)
        height4 = self.driver.execute_script("return arguments[0].naturalHeight", image4)

        if width1 == width2 == width3 == width4 and height1 == height2 == height3 == height4:
            print("Размеры изображений совпадают.")
            print(f"Размеры проверенных изображений:\n image1 {width1} x {height1};\n image2 {width2} x {height2};"
                  f" \n image3 {width3} x {height3};\n image4 {width4} x {height4}.")
        else:
            print("Есть различия!")
            print(f"Размеры изображений следующие: image1 {width1} x {height1};\n image2 {width2} x {height2};"
                  f" \n image3 {width3} x {height3};\n image4 {width4} x {height4}.")

    """Метод скроллинга экрана"""
    def scroll_down(self, x,y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")
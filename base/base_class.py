class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод для получения URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Метод assert word"""

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

        # Или можно по-другому
        # assert title_value == value_for_checking

    """Метод проверки информации о регионе в URL"""
    def check_info_in_URL(self, result = "41-kamchatskij-kraj"): # В данном задании согласно условию выполнения
        get_url = self.driver.current_url              # задания необходима проверка для камчатского края, поэтому я написал
        get_url_str = str(get_url)                     # аргумент по умолчанию (да, не совсем универсально, каюсь :) )
        if result in get_url_str:
            print("Информация о регионе в URL подтверждена успешно")
        else:
            print("Информация о регионе в URL не подтверждена!")

    """Метод assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL соответствует ожидаемому. Проверка прошла успешно")

    """Метод скроллинга экрана"""
    def scroll_down(self, x,y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")
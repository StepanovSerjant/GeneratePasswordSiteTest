from selenium.webdriver.common.by import By

from data.config import TestData
from pages.base_page import BasePage


class MainPageLocators:
    """
    Класс, хранящий все локаторы необходимых
    для работы со страницей элементов
    """

    LENGHT_SELECTOR = (By.ID, "pgLength")
    OPTION_LENGHT_SELECTOR = lambda length: (By.XPATH, f"//option[@value='{str(length)}']")

    SYMBOLS_CHECKBOX = (By.ID, "Symbols")
    NUMBERS_CHECKBOX = (By.ID, "Numbers")
    LOWERCASE_CHECKBOX = (By.ID, "Lowercase")
    UPPERCASE_CHECKBOX = (By.ID, "Uppercase")
    AUTOSELECT_CHECKBOX = (By.ID, "AutoSelect")

    GENERATE_BTN = (By.CSS_SELECTOR, "div.button:nth-child(1)")
    PASSWORD_OUTPUT_FIELD = (By.ID, "final_pass")


class MainPage(MainPageLocators, BasePage):
    """ Класс, описывающий основные действия на странице """
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def set_checkbox(self, by_locator, checkbox_status):
        if self.checkbox_status(by_locator) != checkbox_status:
            self.do_click(by_locator=by_locator)

    def set_length(self, length: int):
        self.do_click(by_locator=MainPage.LENGHT_SELECTOR)
        option = self.wait_for_element(
            MainPage.OPTION_LENGHT_SELECTOR(length), "located", 5
        )
        self.do_click(element=option)

    def get_new_password(self):
        self.do_click(by_locator=MainPage.GENERATE_BTN)
        self.driver.implicitly_wait(2)
        new_pass = self.get_input_value(MainPage.PASSWORD_OUTPUT_FIELD)
        return new_pass

    def get_selected_text(self):
        selected_text = self.driver.execute_script(
            """
            var elem = document.activeElement;
            return elem.value.substring(elem.selectionStart, elem.selectionEnd);"""
        )
        return selected_text


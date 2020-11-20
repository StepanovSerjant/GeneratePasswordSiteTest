from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """
    Родительский класс для всех страниц.
    Содержит общие методы для страниц.
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, ec_type):
        if ec_type == "clickable":
            element = wait(self.driver, 15).until(EC.element_to_be_clickable(by_locator))
        elif ec_type == "located":
            element = wait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element

    def do_click(self, by_locator=None, element=None):
        if not element:
            element = self.wait_for_element(by_locator, "clickable")
        element.click()

    def set_checkbox(self, by_locator, checkbox_status):
        element = self.wait_for_element(by_locator, "located")
        if element.is_selected() != checkbox_status:
            self.do_click(element=element)
            
        
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """
    Родительский класс для всех страниц.
    Содержит общие методы для страниц.
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, ec_type, time):
        if ec_type == "clickable":
            element = wait(self.driver, time).until(EC.element_to_be_clickable(by_locator))
        elif ec_type == "located":
            element = wait(self.driver, time).until(EC.visibility_of_element_located(by_locator))
        return element

    def do_click(self, by_locator=None, element=None):
        if not element:
            element = self.wait_for_element(by_locator, "clickable", 10)
        element.click()

    def checkbox_status(self, by_locator):
        checkbox = self.wait_for_element(by_locator, "located", 10)
        return checkbox.is_selected()

            
        
import pytest

from pages.main_page import MainPage
from tests.test_base import BaseTest


class TestMain(BaseTest):
    
    def test_numbers_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.NUMBERS_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert list(filter(lambda x: x in new_password, list("0123456789")))

    def test_symbols_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.SYMBOLS_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert list(filter(lambda x: x in new_password, list("#%$&@*")))

    def test_uppercase_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.UPPERCASE_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert list(filter(lambda x: x in new_password, list(new_password.upper())))

    def test_lowercase_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.LOWERCASE_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert list(filter(lambda x: x in new_password, list(new_password.lower())))

    def test_autoselect_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.AUTOSELECT_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert new_password == self.main_page.get_selected_text()

    def test_no_amb_checkbox(self):
        exclude_symbols = list("""{[}]()/\'"`~,;:.<>""")
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.NO_AMB_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert not list(filter(lambda x: x in new_password, exclude_symbols))

    def test_no_similar_checkbox(self):
        self.main_page = MainPage(self.driver)
        self.main_page.set_checkbox(self.main_page.NO_SIMILAR_CHECKBOX, True)
        new_password = self.main_page.get_new_password()
        assert not list(filter(
            lambda x: x in new_password and x.upper() in new_password, list(new_password.lower())
        ))

    @pytest.mark.parametrize("length", [6, 10, 12, 16, 17, 66, 78, 120])
    def test_selecting_length(self, length):
        self.main_page = MainPage(self.driver)
        self.main_page.set_length(length)
        new_password = self.main_page.get_new_password()
        assert len(new_password) == length

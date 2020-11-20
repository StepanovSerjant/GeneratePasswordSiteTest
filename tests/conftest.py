import os

import pytest
from selenium import webdriver
from fake_useragent import UserAgent

from data.config import TestData


@pytest.fixture(params=["firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        pass

    if request.param == "firefox":
        # options = webdriver.FirefoxOptions()
        # options.add_argument("start-maximized")
        # options.add_argument(TestData.FIREFOX_PROFILE_PATH)
        # options.set_preference("general.useragent.override", UserAgent().firefox) 
        # options.set_preference("dom.webdriver.enabled", False)

        web_driver = webdriver.Firefox(
            executable_path=TestData.FIREFOX_DRIVER_PATH,
            # firefox_options=options,
        )

    request.cls.driver = web_driver
    yield
    web_driver.close()


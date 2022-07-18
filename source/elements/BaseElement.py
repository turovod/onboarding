import re
import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from utils.timeouts import *
from utils.errors import *


class BaseElement:
    def __init__(self,
                 driver,
                 locator: tuple = (str(), str()),
                 timeout: int = TIMEOUT_DEFAULT,
                 e=None):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, timeout)
        self._locator = locator
        self._e = e if e else self.__find()

    def __find(self, locator=None):
        __locator = locator if locator else self._locator
        try:
            element = self._wait.until(ec.presence_of_element_located(__locator))

            if element:
                return element
        except TimeoutException:
            raise NoSuchElementException(ELEMENT_EXC_MSG)

    @allure.step("Клик")
    def click(self):
        try:
            wait = WebDriverWait(self._driver, TIMEOUT_THREE)
            wait.until(ec.element_to_be_clickable(self._e)).click()
        except WebDriverException:
            raise WebDriverException(CLICK_EXC_MSG)

    @allure.step("Заполнение")
    def fill(self, content: str, clear: bool = True):
        if clear:
            self.clear()
        self._e.send_keys(content)
        return self

    def clear(self):
        self._e.send_keys(Keys.CONTROL + "a")
        self._e.send_keys(Keys.DELETE)
        return self

    def text(self) -> str:
        return re.sub(' +', ' ', self._e.text.strip())

    def get_element_by_locator(self, locator: tuple):
        self.__find(locator)

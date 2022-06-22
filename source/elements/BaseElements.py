from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from source.elements import BaseElement
from utils.errors import *
from utils.timeouts import *


class BaseElements:
    def __new__(cls, driver,
                locator: tuple = (str(), str()),
                timeout: int = TIMEOUT_DEFAULT) -> list[BaseElement]:

        def __find():
            try:
                wait = WebDriverWait(driver, timeout)
                elements = wait.until(ec.presence_of_all_elements_located(locator))
                base_elements = []
                if elements:
                    for index, e in enumerate(elements):
                        current_locator = (locator[0], f"{locator[1]}[{index + 1}]")
                        base_elements.append(BaseElement(driver=driver, locator=current_locator, e=e))
                    return base_elements
            except TimeoutException:
                raise NoSuchElementException(ELEMENT_EXC_MSG)

        return __find()

import pytest
from selenium.webdriver.common.by import By

from source.elements import BaseElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from utils.errors import ELEMENT_EXC_MSG
from utils.timeouts import TIMEOUT_DEFAULT

PARAMS = [
    (By.CSS_SELECTOR, 'div.home-logo__default'),
    (By.CSS_SELECTOR, 'div.home-logo__default123')
]


@pytest.mark.parametrize("locator_type,locator", PARAMS)
def test_get_no_such_element_exception(driver, locator_type, locator):
    element = BaseElement(driver, (locator_type, locator))
    assert element, 'No such element exception'


@pytest.mark.parametrize("locator_type,locator", PARAMS)
def test_exception_handling_with_try_except(driver, locator_type, locator):
    try:
        element = WebDriverWait(driver, timeout=TIMEOUT_DEFAULT).until(
            ec.presence_of_element_located((locator_type, locator)))
        if element:
            return element
    except TimeoutException:
        raise NoSuchElementException(ELEMENT_EXC_MSG)

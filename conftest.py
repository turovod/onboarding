from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
import allure
from uuid import uuid4


@pytest.fixture
def login() -> bool:
    token = "\nToken for authorization: " + str(uuid4())

    print(token)

    yield token

    token = "\nToken for authorization destroyed!"

    print(token)


def __driver(request):
    driver = webdriver.Chrome(executable_path=Path('.') / 'conf' / "chromedriver.exe")
    driver.get("https://yandex.ru/")
    yield driver
    driver.quit()


@allure.title("Экземпляр драйвера")
@pytest.fixture
def driver(request):
    yield from __driver(request)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    when = outcome.get_result().when
    result = outcome.get_result().outcome
    if when in ("setup", "call") and result == "failed":
        args = item.funcargs

        if "driver" in args:
            name = "driver"
        else:
            return

        try:
            allure.attach(
                args[name].get_screenshot_as_png(),
                name=f'Скриншот падения',
                attachment_type=allure.attachment_type.PNG)
        except InvalidSessionIdException:
            return

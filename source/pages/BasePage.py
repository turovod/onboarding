import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Создание скриншота")
    def make_screenshot(self) -> bytes:
        return self.driver.get_screenshot_as_png()

    def attach_screenshot(self, name: str = 'Скриншот', screenshot=None):
        with allure.step(f'Прикрепление скриншота "{name}"'):
            allure.attach(
                self.make_screenshot() if not screenshot else screenshot,
                name=name,
                attachment_type=allure.attachment_type.PNG)

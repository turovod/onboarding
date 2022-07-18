import allure

from source.elements import BaseElements, BaseElement
from source.pages.BasePage import BasePage
from source.locators.TranslatePage import TranslatePageLocators
from utils.errors import *


class TranslatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажатие на кнопку меню примеров")
    def click_examples_menu_button(self, number_button: int, text_button: str) -> object:
        examples_menu_button = BaseElement(self.driver, (TranslatePageLocators.EXAMPLES_MENU_BUTTON[0],
                                                         TranslatePageLocators.EXAMPLES_MENU_BUTTON[
                                                             1] + f'[{number_button}]'))
        if examples_menu_button.text() == text_button:
            examples_menu_button.click()
        else:
            raise ValueError(ELEMENT_TXT_EXC_MSG)
        return examples_menu_button

    @allure.step("Поиск элементов по локатору")
    def search_elements_by_locator(self, locator: tuple = (str(), str())) -> object:
        return BaseElements(self.driver, locator)

    @allure.step("Поиск примеров перевода по локатору")
    def search_examples_by_locator(self) -> object:
        return BaseElements(self.driver, TranslatePageLocators.EXAMPLE_ITEMS_LINC)

    @allure.step("Возврат результата перевода")
    def get_translation(self):
        return BaseElement(self.driver, TranslatePageLocators.EXAMPLE_ITEMS_LINC).text()

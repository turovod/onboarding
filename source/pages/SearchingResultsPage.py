import time

import allure

from source.elements import BaseElements, BaseElement
from source.pages.BasePage import BasePage
from source.locators.SearchingResultsPage import SearchingResultPageLocators as SRPLocators


class SearchingResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажатие на первый найденный элемент на странице")
    def click_first_found_element(self):
        BaseElement(self.driver, SRPLocators.SEARCHING_ITEM_LINK).click()
        time.sleep(5)  # Просто чтобы увидеть открытый сайт

    @allure.step("Нажатие элемент на странице с индексом {number}")
    def click_found_element_with_number(self, number: int):
        items = BaseElements(self.driver, SRPLocators.SEARCHING_ITEM_LINK)
        items[number].click()
        time.sleep(5)  # Просто чтобы увидеть открытый сайт

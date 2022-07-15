import allure

from source.elements import BaseElement
from source.pages.BasePage import BasePage
from source.locators.MainPage import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение поисковой строки текстом")
    def fill_search_field(self):
        BaseElement(self.driver, MainPageLocators.SEARCHING_BOX).fill("Page Object Model" + Keys.ENTER)

    @allure.step("Заполнение поисковой строки произвольным текстом")
    def fill_search_field_arbitrary_text(self, search_text):
        BaseElement(self.driver, MainPageLocators.SEARCHING_BOX).fill(search_text + Keys.ENTER)

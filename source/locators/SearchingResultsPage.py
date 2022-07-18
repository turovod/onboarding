from selenium.webdriver.common.by import By


class SearchingResultPageLocators:
    SEARCHING_ITEM_LINK = By.XPATH, "//li[@class='serp-item serp-item_card']//a"
    TRANSLATOR_ITEM_LINK = By.XPATH, '//*/text()[normalize-space(.)="Переводчик"]/parent::*'

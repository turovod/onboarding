from selenium.webdriver.common.by import By


class TranslatePageLocators:
    EXAMPLE_ITEMS_LINC = By.CSS_SELECTOR, 'div.example_item.example_item_type_book'
    EXAMPLES_MENU_BUTTON = By.XPATH, '//div[@id="examples"]/div[2]/div/button'
    TRANSLATION_RESULT_LINC = By.XPATH, '//pre[@id="translation"]/span/span'


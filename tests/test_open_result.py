from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage


def test_click_first_result(driver):
    MainPage(driver).fill_search_field()
    SearchingResultsPage(driver).click_first_found_element()


def test_click_result(driver):
    MainPage(driver).fill_search_field()
    SearchingResultsPage(driver).click_found_element_with_number(3)

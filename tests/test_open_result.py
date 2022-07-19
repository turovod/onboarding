from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage


def test_click_first_result(driver, login):
    main_page = MainPage(driver)
    main_page.fill_search_field()

    results_page = SearchingResultsPage(driver)
    results_page.click_first_found_element()
    main_page.attach_screenshot('result_scr')


def test_click_first_result_with_search_text(driver, login):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text='turovod.ru')

    results_page = SearchingResultsPage(driver)
    results_page.click_found_element_with_number(3)


def test_click_result(driver, login):
    main_page = MainPage(driver)
    main_page.fill_search_field()

    results_page = SearchingResultsPage(driver)
    results_page.click_found_element_with_number(3)






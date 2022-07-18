from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage
from source.pages.TranslatePage import TranslatePage


def test_get_examples(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text='кошка')

    results_page = SearchingResultsPage(driver)
    results_page.go_to_translator()
    driver.switch_to.window(driver.window_handles[1])
    TranslatePage(driver).click_examples_menu_button(number_button=2, text_button='cat')
    examples = TranslatePage(driver).search_examples_by_locator()
    assert 'It was not the only cat' in examples[0].text()


def test_word_translation(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text='слон')

    results_page = SearchingResultsPage(driver)
    results_page.go_to_translator()
    driver.switch_to.window(driver.window_handles[1])
    translation_result = TranslatePage(driver).get_translation()
    print('*' * 50)
    print(translation_result)
    assert translation_result == 'elephant', f'"{translation_result}"  is not as expected "elephant"'

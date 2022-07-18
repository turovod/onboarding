from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage
from source.pages.TranslatePage import TranslatePage


def test_translate_dog_into_english(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text='собака')

    results_page = SearchingResultsPage(driver)
    results_page.go_to_translator()
    driver.switch_to.window(driver.window_handles[1])
    TranslatePage(driver).click_examples_menu_button(number_button=2, text_button='dog')
    examples = TranslatePage(driver).search_examples_by_locator()

    for example in examples:
        assert 'dog' in example.text(), f'The example "{examples}" does not contain the word "dog"'

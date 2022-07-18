import pytest

from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage
from source.pages.TranslatePage import TranslatePage
from source.model.TranslatePage import WordsForTranslationTest as words


def test_get_examples(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text='кошка')

    results_page = SearchingResultsPage(driver)
    results_page.go_to_translator()
    driver.switch_to.window(driver.window_handles[1])
    TranslatePage(driver).click_examples_menu_button(number_button=2, text_button='cat')
    examples = TranslatePage(driver).search_examples_by_locator()
    assert 'It was not the only cat' in examples[0].text()


@pytest.mark.parametrize("test_input,expected", words().get_test_word_pairs())
def test_get_translate(driver, test_input: str, expected: str):
    main_page = MainPage(driver)
    main_page.fill_search_field_arbitrary_text(search_text=test_input)

    results_page = SearchingResultsPage(driver)
    results_page.go_to_translator()
    driver.switch_to.window(driver.window_handles[1])
    TranslatePage(driver).click_examples_menu_button(number_button=2, text_button=expected)
    examples = TranslatePage(driver).search_examples_by_locator()

    for example in examples:
        assert expected in example.text(), f'The example "{example}" does not contain the word "{expected}"'



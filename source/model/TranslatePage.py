class WordsForTranslationTest:
    def __init__(self):
        self.dictionary_words = {
            "помидор": "tomato",
            "книга": "book",
            "conftest": "конфтест",
            "banana": "банан"
        }

    def get_test_word_pairs(self):
        return list(zip(self.dictionary_words.keys(), self.dictionary_words.values()))
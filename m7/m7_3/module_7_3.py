import os
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read()

                clean_text = (text.replace(',', ' ').replace('.', ' ')
                              .replace('!', ' ').replace('?', ' ')
                              .replace('=', ' ').replace(':', ' ')
                              .replace(';', ' ').replace(' - ', ' ').lower())

                words = clean_text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        result = {}

        for file_name, words in self.get_all_words().items():
            try:
                index = words.index(word.lower())
                result[file_name] = index + 1
            except ValueError:
                pass

        return result

    def count(self, word):
        result = {}

        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower())

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
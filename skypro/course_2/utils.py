import random

from config import WORDS_JSON_SOURCE
import requests as requests

from skypro.course_2.basic_word import BasicWord


def load_random_word(json_source):
    """Загружает случайное слово из указанного списка и возвращает экземпляр класса BasicWord"""
    result = requests.get(json_source)
    result_data = result.json()
    word_data = random.choice(result_data)
    basic_word = BasicWord(**word_data)
    # basic_word = BasicWord(word=word_data["word"], subwords=word_data["subwords"]) тоже самое, что и верхняя строка
    return basic_word


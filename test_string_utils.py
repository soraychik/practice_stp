"""
Тесты для string_utils
"""
import pytest
from string_utils import *


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("123") == "321"
    assert reverse_string("") == ""


def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is awesome") == "Python Is Awesome"


def test_contains_substring():
    assert contains_substring("hello world", "world") == True
    assert contains_substring("hello", "xyz") == False


# Намеренно падающий тест для демонстрации CI/CD
def test_failing_for_demo():
    """Этот тест упадет - для демонстрации CI/CD"""
    assert 2 + 2 == 4  # ОШИБКА: должно быть 4!

"""
Простая библиотека для работы со строками
"""

def reverse_string(s: str) -> str:
    """Переворачивает строку"""
    return s[::-1]


def count_vowels(s: str) -> int:
    """Считает количество гласных в строке"""
    vowels = "aeiouаеёиоуыэюя"
    return sum(1 for char in s.lower() if char in vowels)


def is_palindrome(s: str) -> bool:
    """Проверяет, является ли строка палиндромом"""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    """Делает каждое слово с заглавной буквы"""
    return ' '.join(word.capitalize() for word in s.split())


def contains_substring(s: str, substring: str) -> bool:
    """Проверяет, содержит ли строка подстроку"""
    return substring in s
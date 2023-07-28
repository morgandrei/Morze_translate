from random import choice
import json


def get_json():
    """Получаем коды морзе из файла"""
    with open('src\morze.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def morse_encode(word, morse_code):
    """Функция кодирования слова"""
    encrypted_word = ""
    for i in word:  # Запускаем цикл по перебору букв в слове
        encrypted_word += morse_code[i] + " "  # Заменяем букву в слове и добавляем пробел
    return encrypted_word


def get_word(words_for_encoding):
    """Получаем случайное слово из списка"""
    random_word = choice(words_for_encoding)
    return random_word


def print_statistics(answers):
    """Функция вывода статистики"""
    true_answers = 0  # Счетчик правильных ответов
    false_answers = 0  # Счетчик неправильных ответов
    for i in answers:  # Запускаем цикл по перебору списка ответов

        if i == True:
            true_answers += 1

        else:
            false_answers += 1

    # Переменная stats собирает в себе информацию для вывода
    stats = "\nВсего задачек: " + str(len(answers)) + "\nОтвечено верно: " + str(
        true_answers) + "\nОтвечено неверно: " + str(false_answers)

    return stats

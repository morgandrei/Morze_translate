from src.utils import morse_encode, get_word, print_statistics, get_json

morse_code = get_json()  # Загружаем словарь с расшифровкой азбуки Морзе
words_for_encoding = ["code", "bit", "list", "soul", "next", "little", "snake", "wellplayed"]  # Список слов для кодирования
quest_count = 1  # Счетчик вопросов
answers = []  # Список статистики

input("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")

# Запускаем цикл с пятью вопросами
while quest_count <= 5:

    word = get_word(words_for_encoding)  # Присваиваем случайное слово
    encrypted_word = morse_encode(word, morse_code)  # Присваиваем зашифрованное слово

    # Присваиваем введенное пользователем слово
    user_word = input(f"\nСлово {quest_count}: {encrypted_word}")

    if user_word == word:  # Если введенное слово соответсвует зашифрованному слову
        print(f"Верно, {word}!")
        answers.append(True)  # Записывает в список статистики правильный ответ


    else:  # Если не соответствует
        print(f"Неверно, {word}!")
        answers.append(False)  # Записывает в список статистики правильный ответ

    quest_count += 1  # Увеличиваем счетчик вопросов на единицу

print(print_statistics(answers))  # Выводим статистику


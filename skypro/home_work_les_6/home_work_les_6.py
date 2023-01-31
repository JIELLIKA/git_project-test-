import random
"""Задаем переменные, необходимые для дальнейшей работы"""
user_name = input("Введите Ваше имя:")
score = 0
game_count = 0
max_result = 0

"""Берем из файла каждое слово по очереди, перемешиваем буквы, выводим пользователю,
получаем ответ. В случае правильного ответа начисляем 10 балов, в случае неправильного - выводим правильный ответ"""

with open ('words.txt', encoding='utf-8') as file:
    for line in file:
        origin_word = line.rstrip('\n')
        origin_word_to_convert = list(origin_word)
        random.shuffle(origin_word_to_convert)
        new_word = ''.join(origin_word_to_convert)
        print(f"Угадайте слово: {new_word}")
        user_answer = input()
        if user_answer == origin_word:
            print("Верно! Вы получаете 10 очков")
            score += 10
        else:
            print(f"Неверно! Правильное слово - {origin_word}")
    total_score = str(score)
    result = open('history.txt', 'a')
    result.write(f"{user_name}:")
    result.write(f"{total_score}\n")
    result.close()

"""Выводим общее количество игр и максимально дистигнутый результат"""

with open ('history.txt') as file:
    for item_data in file:
        game_count += 1
        name, result = item_data.strip().split(':')
        convert_result = int(result)
        if convert_result > max_result:
            max_result = convert_result
    print(f"Всего игр сыграно: {game_count}")
    print(f"Максимальный результат: {max_result}")

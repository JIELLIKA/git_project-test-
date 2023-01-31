from config import WORDS_JSON_SOURCE
from skypro.course_2 import utils
from skypro.course_2.player import Player


def main():
    print("Введите имя игрока")
    user_input = input().strip().title()
    basic_word = utils.load_random_word(WORDS_JSON_SOURCE)

    player = Player(name=user_input)
    print(f"Привет, {player.get_name()}!")
    print(f"Составьте 8 слов из слова {basic_word.get_word()}\n"
          "Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру угадайте все слова или напишите 'stop'\n"
          "Поехали, ваше первое слово?\n"
          )


    while player.count_used_words() < basic_word.len_sub():

        user_input = input()
        if len(user_input) < 3:
            print("Слишком короткое слово!")
        elif user_input in ["стоп", "stop"]:
            break

        elif player.has_word_used(user_input):
            print("Уже использовано!")

        elif not basic_word.has_subword(user_input):
            print("Неверно!")

        else:
            print("Верно!")
            player.add_word(user_input)

    print(f"Игра завершена. Вы угадали {player.count_used_words()} слов")

if __name__ == "__main__":
    main()
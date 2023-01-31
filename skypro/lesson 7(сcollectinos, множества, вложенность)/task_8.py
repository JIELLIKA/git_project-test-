"""Поиск по спискам — не самая удобная операция,
если значения хранятся внутри словарей. Давайте напишем функцию, которая выполняет поиск.
Обратите внимание, функция должна возвращать два значения: название рыбы и воду, в которой она живет.
Используйте кортеж для этой цели.

Пример вывода: Белуга fresh"""

fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

def get_fish(fish_name):
    for x in fish:
        fish_spec = x['specie']
        water = x['water']
        return fish_spec, water
    pass

# Не удаляйте код ниже, он нужен для проверки!

fish_name = input()
fish, water = get_fish(fish_name)
print(fish, water)
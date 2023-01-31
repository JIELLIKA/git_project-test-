"""Некоторые рыбы предпочитают морскую воду, некоторые — пресную.
Разделите список словарей на два, затем выведите названия вида из каждого словаря в строку.
Вот так:

Морские: Тунец, Скумбрия
Пресноводные: Красноперка, Карась"""

fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for item in fish:
    if item['water'] == "fresh":
        fresh_water.append(item['specie'])
    else:
        sea_water.append(item['specie'])

sea_water_str = ",".join(sea_water)
fresh_water_str = ",".join(fresh_water)
print(f"Морские: {sea_water_str}")
print(f"Пресноводные:  {fresh_water_str}")

"""Одна из типичных задач при работе с данными — перекладывание их из одного формата в другой.
Мы хотим отправить несколько контейнеров с живой рыбой в соседний питомник,
но чтобы занести во внутреннюю систему задачу от внешнего заказчика, нужно перевести заказ из «их формата»
в «наш формат».

Формат заказчика:

{"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300}

Наш формат:

{"count": 5, "specie": "Тунец" , "avg_size": 30 }

Заказчик называет ключи транслитом, хранит количество рыб в типе с точкой,
размер рыбы в миллиметрах, а породу пишет с маленькой буквы. Просто катастрофа, а не заказчик!
Придется писать конвертер."""

order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []
change_key_name = {}

for item in order:
    item['skolko'] = int(item['skolko'])
    item['sred_razmer'] = int(item['sred_razmer'] / 10)
    item['poroda'] = str.title(item['poroda'])
    for key, value in item.items():
        if key == "skolko":
            key = "count"
        if key == "poroda":
            key = "specie"
        if key == "sred_razmer":
            key = "avg_size"
        change_key_name[key] = value
        order_converted.append(change_key_name)
    # print(order_converted)            С этим вся программа работала

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)

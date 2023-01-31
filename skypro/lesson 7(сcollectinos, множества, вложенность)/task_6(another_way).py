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

for i in order:
    order_converted.append({"count": int(i["skolko"])})
    order_converted.append({"specie": str.title(i["poroda"])})
    order_converted.append({"avg_size": int(i["sred_razmer"] / 10)})

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)

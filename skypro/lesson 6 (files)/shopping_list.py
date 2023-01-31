"""Считает по списку покупок количество позиций и итоговую стоимость"""

row_index = 0
items_count = 0
items_sum = 0

with open('shopping_list.txt') as file:
    for item_data in file:
        row_index += 1
        if item_data.count (':') < 2:
            print (f"В строке {row_index} есть ошибка")
            continue

        item, quantity, price = item_data.strip().split(':')
        items_count += 1
        items_sum = int(price) * int(quantity)

    print(f"В списке {items_count} позиций. Сумма {items_sum}р.")
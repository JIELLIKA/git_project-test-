from datetime import date

# Задает первую дату
time_one = date(2020, 10, 1)
# Задает вторую дату
time_two = date(2020, 10, 2)

# Вычисляет расстояние в формате timedelta
delta = time_two - time_one

print(delta)

# Выведет 1 day, 0:00:00
user_language = input("Какой язык вы учите?")
user_time = input("Как давно?")
user_institution = input("Где?")

with open ('answers.txt', 'wt') as file:
    file.write(f"{user_language}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_institution}\n")

print("Ответы записаны")
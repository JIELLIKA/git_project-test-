with open ('students.txt') as file:
    for students_data in file:
        # data = students_data.rstrip('\n').split(':') #rstrip - убирает отмеченный по умолчанию символ справа на перенос строки
        # name = data[0]
        # language = data[1]

        name, language = students_data.rstrip('\n').split(':') #также можно записать все, что записано вверху

        print(f"{name} учит язык {language}!")
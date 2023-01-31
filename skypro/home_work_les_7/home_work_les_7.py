import json

"""Создаем функцию для загрузки списка студентов"""
def load_students():
    with open('students.json') as file:
        raw_json = file.read()
        students = json.loads(raw_json)
        return students

"""Создаем функцию для загрузки списка профессий"""
def load_professions():
    with open('professions.json') as file:
        raw_json = file.read()
        professions = json.loads(raw_json)
        return professions

"""Создаем функцию для возврата информации о студенте по заданному порядковому номеру
 и завершает программу, если введенный номер не соответствует количеству студентов"""
def get_student_by_pk(student):
    student_group = load_students()
    if student > len(student_group):
        print("У нас нет такого студента")
        quit()
    else:
        for i in range(len(student_group)):
            if student == student_group[i]["pk"]:
                return student_group[i]["full_name"], student_group[i]["skills"]

"""Создаем функцию для возврата информации о необходимых навыках для введенной профессии"""
def get_profession_by_title(profession):
    professions_list = load_professions()
    for i in range(len(professions_list)):
        if profession == professions_list[i]["title"]:
            return professions_list[i]["skills"]

"""Создаем функцию для определения соответствия навыков студента и 
требуемых навыков для определенной профессии"""
def check_fitness(student, profession):
    percentage = 0
    stud_inform = {}
    stud_skills = set(stud_lang)
    all_skills = set(get_profession_by_title(profession))
    known_lang = stud_skills.intersection(all_skills)
    lang_to_learn = all_skills.difference(stud_skills)
    percentage = ((len(known_lang) * 100) / (len(known_lang) + len(lang_to_learn)))
    return lang_to_learn, percentage


student = int(input("Введите номер студента:"))
students_name, stud_lang = get_student_by_pk(student)
print(f"Студент {students_name}")
stud_lang_format = " ".join(stud_lang)
print(f"Знает: {stud_lang_format}")
profession = input(f"Введите специальность для оценки студента {students_name}:")
unuxpect_lang, stud_suit = check_fitness(student, profession)
unuxpect_lang_format = " ".join(unuxpect_lang)
print(f"Пригодность: {stud_suit}")
print(f"Студент знает: {stud_lang_format}")
print(f"Студент не знает: {unuxpect_lang_format}")



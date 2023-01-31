"""Задаем переменные для подсчета количества правильных ответов, общего количества вопросов и общего счета"""

import json

total_score = 0
count_correct_answers = 0
count_all_questions = 0
questions = []


class Question():
    def __init__(self, text_question, difficulty, correct_answer):
        self.text_question = text_question
        self.difficulty = difficulty
        self.correct_answer = correct_answer

    def get_points(self):
        """Возвращает int, количество баллов. Баллы зависят от сложности:
        за 1 дается 10 баллов, за 5 дается 50 баллов."""
        return int(self.difficulty) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False."""
        if user_answer == self.correct_answer:
            return True
        else:
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return (f"Вопрос: {self.text_question} \n"
                f" Сложность {self.difficulty}/5 ")

    def build_feedback(self):
        """Возвращает: Ответ верный, получено __ баллов или Ответ неверный, верный ответ ___"""
        if user_answer == self.correct_answer:
            print(f"Ответ верный, получено {int(self.difficulty) * 10} баллов")
        else:
            print(f"Ответ неверный, верный ответ - {self.correct_answer}")


with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item_data in data:
        question = item_data['q']
        difficulty = item_data['d']
        correct_answer = item_data['a']
        question_ = Question(question, difficulty, correct_answer)
        questions.append(question_)

for item in questions:
    count_all_questions += 1
    print(item.build_question())
    user_answer = input()
    item.build_feedback()
    if item.is_correct():
        total_score += item.get_points()
        count_correct_answers += 1

print("Вот и все!")
print(f"Отвечено на {count_correct_answers} из {count_all_questions}")
print(f"Набрано {total_score} баллов")

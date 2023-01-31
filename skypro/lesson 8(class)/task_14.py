"""Создай класс Player с полями:

Имя игрока (name) – строка
Количество очков (score) – целое число, при инициализации всегда 0

Добавь классу метод get_score() который возвращает значение score

Добавь классу метод set_score(<значение>) который задает значение, например, set_score(20).

Создай экземпляр класса Player c именем Алиса"""

class Player:

  def __init__(self, name, score):
      self.name = name
      self.score = score

  def get_score(self):
      return self.score

  def set_score(self, score):
      self.score = score

player_1 = Player("Алиса", 0)


# Не удаляйте этот код, он нужен для проверки

print(player_1.name, player_1.get_score())
player_1.set_score(200)
print(player_1.name, player_1.get_score())
player_1.set_score(500)
print(player_1.name, player_1.get_score())
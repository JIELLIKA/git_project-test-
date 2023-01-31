class Player():
    """Создаем класс, который содержит в себе имя пользователя и количество использованных слов"""
    def __init__(self, name="", used_words=None):
        self.name = name
        if used_words is None:
            self.used_words = []
        else:
            self.used_words = used_words

    def __repr__(self):
        return f'Player(name={self.name}, used_words={self.used_words})'

    def get_name(self):
        """Возвращает имя пользователя"""
        return self.name

    def add_word(self, word):
        """Добавляет слово в список использованных слов"""
        self.used_words.append(word)

    def count_used_words(self):
        """Возвращает количество использованных слов"""
        return len(self.used_words)

    def has_word_used(self, word):
        """Возвращает было ли использовано слово"""
        return word in self.used_words


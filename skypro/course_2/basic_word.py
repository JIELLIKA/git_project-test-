class BasicWord():
    """Класс слова для игры в угадывание слов"""
    def __init__(self, word="", subwords=None):
        self.word = word
        if subwords is None:
            self.subwords = []
        else:
            self.subwords = subwords

    def __repr__(self):
        return f'BasicWord(word={self.word}, subwords= {self.subwords})'

    def get_word(self):
        """Возвращает исходное слово"""
        return self.word

    def len_sub(self):
        """Возвращает общее количество подслов, которые можно составить"""
        return len(self.subwords)

    def has_subword(self, word):
        """Проверяет существует ли введенное слово в исходном слове"""
        return word in self.subwords






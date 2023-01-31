"""Создай класс Album у которого есть поля

Исполнитель (artist) - строка
Название (title) - строка
Треки (tracks) - это список
Создай два экземпляра album_1 и album_2

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou"""


class Album:

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.tracks = []

    def music_albums(self, track):
        self.tracks.append(track)


album_1 = Album("Queen", "Killer Queen")
album_1.music_albums("Killer Queen")
album_1.music_albums("Brighton rock")
album_1.music_albums("Tenement Funster")
album_2 = Album("Metallica", "Black Album")
album_2.music_albums("Enter Sandman")
album_2.music_albums("Sad But True")
album_2.music_albums("Holier Than Thou")

# Не удаляйте этот код, он нужен для проверки

print(album_1.artist, album_1.title, len(album_1.tracks), "треков")
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")

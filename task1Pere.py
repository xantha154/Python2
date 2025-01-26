class Book:
    """Базовый класс книги."""
    # Метод инициализации для базового класса Book
    def __init__(self, name: str, author: str):
        self._name = name #Название книги
        self._author = author #Автор книги

    @property
    def name(self):
        return self._name #Свойство для получения названия книги

    @property
    def author(self):
        return self._author #Свойство для получения имени автора книги

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}" #Метод для строкового представления объекта

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int): #Метод инициализации бумажной книги с указанием количества страниц
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self): #Свойство для получения количества страниц
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self): #Метод для строкового представления бумажной книги
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float): #Метод инициализации аудиокниги с указанием длительности
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self): #Свойство для получения длительности аудиокниги
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = float(value)

    def __str__(self): #Метод для строкового представления аудиокниги
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration:.2f} часов"
# Пример использования
try:
    # Создание бумажной книги
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    print(paper_book)
    print(repr(paper_book))
    # Создание аудиокниги
    audio_book = AudioBook("1984", "Джордж Оруэлл", 10.5)
    print(audio_book)
    print(repr(audio_book))
    # Установка некорректного количества страниц
    paper_book.pages = -100  # Должно вызвать ValueError
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
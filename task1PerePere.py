class Book:
    """Базовый класс книги. Содержит общие свойства: название и автор."""

    def __init__(self, name: str, author: str):
        """Инициализация базового класса Book."""
        self._name = name  # Название книги
        self._author = author  # Автор книги

    @property
    def name(self):
        """Возвращает название книги."""
        return self._name

    @property
    def author(self):
        """Возвращает имя автора книги."""
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для валидации

    @property
    def pages(self):
        """Возвращает количество страниц книги."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Устанавливает количество страниц книги с проверкой корректности."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга '{self.name}'. Автор: {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для валидации

    @property
    def duration(self):
        """Возвращает длительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Устанавливает длительность аудиокниги с проверкой корректности."""
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига '{self.name}'. Автор: {self.author}. Длительность: {self.duration:.2f} часов"


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

    # Установка корректного и некорректного значения страниц
    paper_book.pages = 500  # Корректное значение
    print(f"Количество страниц изменено: {paper_book.pages}")
    paper_book.pages = -100  # Некорректное значение, вызовет ValueError
except (TypeError, ValueError, AttributeError) as e:
    print(f"Ошибка: {e}")
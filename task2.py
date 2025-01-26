BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_ # id книги
        self.name = name # название книги
        self.pages = pages # количество страниц
    def __str__(self):
        return f'Книга "{self.name}"' # строковый вид
    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books=None): # инициализация библиотеки
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books: # если в библиотеке нет книг
            return 1
        return max(book.id for book in self.books) + 1 # максимальный id + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [ # создает список обьектов
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

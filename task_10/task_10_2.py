class Book:
    def __init__(self, name, autor, publish_year, genre):
        self.name = name
        self.autor = autor
        self.publish_year = publish_year
        self.genre = genre

    def book_info(self):
        print(f"Название книги - {self.name}\n"
              f"Автор - {self.autor}\n"
              f"Год издания - {self.publish_year}\n"
              f"Жанр - {self.genre}\n")


my_book = Book("Гиперион", "ден Симмонс", "1997", "Фантастика")
my_book.book_info()

# Название книги - Гиперион
# Автор - ден Симмонс
# Год издания - 1997
# Жанр - Фантастика

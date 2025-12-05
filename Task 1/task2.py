class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Вы взяли книгу: {self}")
        else:
            print(f"Книга {self} не доступна")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Вы вернули книгу: {self}")
        else:
            print(f"Книга {self} уже доступна")

    def get_info(self):
        return self.__str__()
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}, {self.is_available}"

def main():
    book1 = Book("Fool", "James A.K.", "1994")
    book2 = Book("Genius", "Martin L.F.", "2003")
    book3 = Book("Fool 2. Reprise", "James A.K.", "1997")
    print(book1.get_info())
    book1.borrow();
    print(book1.get_info())
    book1.return_book()
    print(book1.get_info())
    print(book2.get_info())
    print(book3.get_info())

if __name__ == '__main__':
    main()
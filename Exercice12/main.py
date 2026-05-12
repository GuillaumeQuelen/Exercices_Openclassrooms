class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []
        
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return
        print("Titre non trouvé")
    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return
        print("Titre non trouvé")
    def return_book(self, book_title):
        for book in self.borrowed_books:  # cherche dans les empruntés
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return
        print("Titre non trouvé")
    def available_books(self):
        return [book.title for book in self.books]
    def borrowed_books(self):
        return [book.title for book in self.borrowed_books]
    # Ajouter les méthodes ici
# Test
library = Library()
book1 = Book("Le Petit Prince", "Saint-Exupéry", 1943)
book2 = Book("1984", "Orwell", 1949)
library.add_book(book1)
library.add_book(book2)
library.borrow_book("1984")
print(library.available_books())
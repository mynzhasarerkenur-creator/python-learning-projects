import json

class Books:
    def __init__(self, name_book, avtor, pages):
        self.name_book = name_book
        self.pages = pages
        self.avtor = avtor

    def show_books(self):
        print(f"name: {self.name_book}, avtor: {self.avtor}, pages: {self.pages}")

    def to_dict(self):
        return {'name_book': self.name_book, 'avtor': self.avtor, 'pages': self.pages }
    
books = []
try:
    with open('books.json','r') as files:
        book_data = json.load(files)
        for data in book_data:
            books.append(Books(data['name_book'],data['avtor'], data['pages']))
except FileNotFoundError:
    book_data = []
while True:
    print('1 - добавить книгу')
    print('2 - показать книги')
    print('3 - выйти')

    choise = input("выбор: ")
    
    if choise == '1':
        name_book = input('название книги: ')
        avtor = input('автор книги: ')
        pages = int(input('страницы книги: '))
        books.append(Books(name_book,avtor,pages))
    
    elif choise == '2':
        if not books:
            print('No books')
        else:
            for book in books:
                book.show_books()
    elif choise =='3':
        book_data = []
        for book in books:
            book_data.append(book.to_dict())
        with open('books.json', 'w') as files:
            json.dump(book_data,files, indent= 3)
        break


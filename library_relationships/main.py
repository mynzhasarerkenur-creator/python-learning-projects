import storage

storage.create_table()

while True:
    print(
        "1. - add user\n" \
        "2. - add book\n" \
        "3. - show users\n" \
        "4. - show books\n" \
        "5. - borrow book\n" \
        "6. - show borrow details\n" \
        "7. - return book\n" \
        "8. - exit"
    )

    choise = input("РІС‹Р±РѕСЂ: ")

    if choise == '1':
        name_input = input('name user: ') 
        storage.add_user(name_input)
        print('succes')

    elif choise == '2':
        title_input = input("book title: ")
        author_input = input('book author: ')
        storage.add_book(title_input, author_input)

    elif choise == '3':
        users = storage.show_data_users()
        if not users:
            print('users is empty')
        else:
            for user in users:
                print(user[0])
                print(user[1])
                print()
        
    elif choise == '4':
        books = storage.show_data_books()
        if not books:
            print('books is empty')
        for book in books:
            print(book[0])
            print(book[1])
            print(book[2])
    
    elif choise == '5':
        title_input = input('books title: ')
        books = storage.search_title_book(title_input)
        if not books:
            print('book title is not found')
        else:
            for book in books:
                print(f'code: {book[0]}')
                print(f'title: {book[1]}')
                print(f'author: {book[2]}')
                print()
            while True:
                try:
                    code_book_input = int(input('write books code: '))
                    user_name_input = input('user name: ')
                    break
                except ValueError:
                    print("РІРІРµРґРёС‚Рµ РєРѕСЂСЂРµРєРЅС‹Рµ РґР°РЅРЅС‹Рµ")

            user = storage.check_user(user_name_input)
            if user is None:
                print("user is not found")
                continue
            user_id = user[0]

            book = storage.check_book(code_book_input)
            if book is None:
                print("book is not found")
                continue
            book_id = book[0]

            borrowed = storage.check_borrowed(book_id,user_id)
            if borrowed is not None:
                print("book is already borrowed")
                continue

            result = storage.add_borrow_book(book_id, user_id)
            if result == "success":
                print("the book was successfully issued")

        
    elif choise == '6':
        borrowes = storage.show_borrowed_details()
        if not borrowes:
            print('borrowes is not found')
        else:
            for borrow in borrowes:
                print(f'{borrow[0]} borrow is: ')
                print(borrow[1])
                print(borrow[2])
    
    elif choise == '7':
        while True:
            name_input = input('user name: ')
            user = storage.check_user(name_input)
            if user is None:
                print("user is not found")
                continue
            user_id = user[0]
            boorrowes = storage.search_borrowed_books(user_id)
            for borrow in boorrowes:
                print(borrow[1])
                print(borrow[2])
                print(borrow[3])
                print('________________')
            code_book_input = input('books code: ')
            result = storage.check_book(code_book_input)
            if result is None:
                print('book code is incorrect')
                continue
            book_id = result[0]
            result = storage.return_book(user_id, book_id)
            if result == "success":
                print("book returned successfully")
                break

    elif choise =='8':
        break


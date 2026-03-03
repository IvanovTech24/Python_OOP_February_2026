from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str , list[str]] = {} # {"author": ["book_1", "book_2", ...]}
        self.rented_books: dict[str, dict[str, int]] = {} # {"Ivan": {"book_1": 2, "book_2": 5, ...}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {book_name: days_to_return}
            else:
                self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            days = 0
            for rented_info in self.rented_books.values():
                if book_name in rented_info:
                    days = rented_info[book_name]
                    break
            return f'The book "{book_name}" is already rented and will be available in {days} days!'


    def return_book(self, author:str, book_name:str, user: User) -> str | None:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"

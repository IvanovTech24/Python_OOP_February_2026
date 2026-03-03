from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library) -> str:
        if user not in library.user_records:
            library.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> str:
        if user in library.user_records:
            library.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for curr_user in library.user_records:
            if curr_user.user_id == user_id:
                if new_username != curr_user.username:
                    if curr_user.username in library.rented_books.keys():
                        library.rented_books[new_username] = library.rented_books[curr_user.username]
                        del library.rented_books[curr_user.username]
                    curr_user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"

class NotAvailableEmail(Exception):
    pass


class Spotipy:
    def __init__(self):
        self.__users = []

    def register_user(self, new_user):
        if self.__is_available_email(new_user.email):
            self.__users.append(new_user)
            return new_user
        else:
            raise NotAvailableEmail(new_user.email)

    def __is_available_email(self, email):
        repeated = list(filter(lambda u: u.email == email, self.__users))

        return len(repeated) == 0

    def is_registered(self, new_user):
        return new_user.email in list(map(lambda u: u.email, self.__users))

    def login(self, user):
        if self.is_registered(user):
            return True

        return False


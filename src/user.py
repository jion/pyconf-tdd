class User:
    def __init__(self, email, name, lastname):
        self.__email = email
        self.__name = name
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name

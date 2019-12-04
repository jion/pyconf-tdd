import sys
sys.path.insert(0,'./src')

import unittest
from user import User
from spotipy import Spotipy, NotAvailableEmail


class UserRegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.__spotipy = Spotipy()
        pepe_email = "jose_perez@gmail.com"
        pepe_name = "Jose"
        pepe_lastname = "Perez"

        self.new_user = User(pepe_email, pepe_name, pepe_lastname)

    def test_usuario_sin_cuenta_se_registra_con_mail_disponible(self):

        self.__spotipy.register_user(self.new_user)
        expected_response = self.__spotipy.is_registered(self.new_user)

        self.assertTrue(expected_response)

    def test_usuario_se_registra_con_email_duplicado_lanza_exception(self):
        self.__spotipy.register_user(self.new_user)  # User registers for first time

        with self.assertRaises(NotAvailableEmail):
            self.__spotipy.register_user(self.new_user)


class UserLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.__spotipy = Spotipy()
        pepe_email = "jose_perez@gmail.com"
        pepe_name = "Jose"
        pepe_lastname = "Perez"

        self.new_user = User(pepe_email, pepe_name, pepe_lastname)
        self.registered_user = self.__spotipy.register_user(self.new_user)

    def test_usuario_con_cuenta_se_loguea(self):

        response = self.__spotipy.login(self.registered_user)

        self.assertTrue(response)

    def test_usuario_sin_cuenta_intenta_loguearse(self):
        non_existent_user = User("newuser@gmail.com", "name", "last")

        response = self.__spotipy.login(non_existent_user)

        self.assertFalse(response)


if __name__ == '__main__':
    unittest.main()

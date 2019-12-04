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
        self.__spotipy.register_user(self.new_user)  # First time

        with self.assertRaises(NotAvailableEmail):
            self.__spotipy.register_user(self.new_user)  # First time


if __name__ == '__main__':
    unittest.main()

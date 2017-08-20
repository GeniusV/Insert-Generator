import unittest

from genrators.PasswordGenerator import PasswordFactory
from Generator import DateGenerator


class PasswordFactoryTest(unittest.TestCase):
    def test_password_factory(self):
        DateGenerator("test", {"test": PasswordFactory()}, 100).run()

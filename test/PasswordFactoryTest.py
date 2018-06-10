import unittest

from generators.IdFactory import IdFactory
from generators.NameFactory import ZHNameFactory
from generators.PasswordFactory import PasswordFactory
from Generator import DateGenerator
from generators.RandNumFactory import RandNumFactory


class PasswordFactoryTest(unittest.TestCase):
    def test_password_factory(self):
        DateGenerator("test", {"test": PasswordFactory()}, 100).run()

    def test_name(self):
        DateGenerator('student', {'id': IdFactory(51), 'name': ZHNameFactory(), 'password': '123456', 'claxx_id': 2}, 50).run()

    def test_num(self):
        DateGenerator('score', {'id': IdFactory(start = 1), 'value': RandNumFactory(), 'course_id': 1, 'student_id': IdFactory(1), 'term_id': 1}, 100).run()

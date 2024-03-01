from unittest import TestCase
from oop2.diaries import Diaries


class TestDiariesFunction(TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_add(self):
        self.diaries.add("username", "password")
        self.assertEqual(len(self.diaries.get_length()), 1)

    def test_find_by_user_name(self):
        self.diaries.add("username", "password")
        found_dairy = self.diaries.find_by_user_name("username")
        self.assertEqual("username", found_dairy.user_name)

    def test_delete(self):
        self.diaries.add("username", "password")
        self.diaries.remove("username", "password")
        self.assertEqual(len(self.diaries.get_length()), 0)

    def test_add_twice(self):
        self.diaries.add("username", "password")
        self.diaries.add("username1", "password1")
        self.assertEqual(len(self.diaries.get_length()), 2)

    def test_add_twice_delete_one(self):
        self.diaries.add("username", "password")
        self.diaries.add("username1", "password1")
        self.assertEqual(len(self.diaries.get_length()), 2)
        self.diaries.remove("username", "password")
        self.assertEqual(len(self.diaries.get_length()), 1)

    def test_find_two_user_by_name(self):
        self.diaries.add("username", "password")
        self.diaries.add("username1", "password1")
        found_dairy = self.diaries.find_by_user_name("username")
        found_dairy1 = self.diaries.find_by_user_name("username1")
        self.assertEqual("username", found_dairy.user_name)
        self.assertEqual("username1", found_dairy1.user_name)




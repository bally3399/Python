import unittest
import ascending_order

class TestAscendingFunction(unittest.TestCase):
    def test_that_function_is_not_none(self):
        self.assertIsNotNone(ascending_order.ascending_order)

    def test_that_function_sort_array_in_ascending_order(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        sample_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sample_output, ascending_order.ascending_function(sample_list))

class TestDescendingFunction(unittest.TestCase):
    def test_that_function_sort_array_in_descending_order(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        sample_output = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(sample_output, descending_order(sample_list))


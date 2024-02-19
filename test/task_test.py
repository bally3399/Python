import task
import pytest

def test_length():
    assert task.length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10

def test_add_even():
    assert task.add_even() == 30

def test_add_odd():
    assert task.add_odd() == 25

def test_multiplication():
    assert task.multiplication() == 945

def test_average_of_list():
    assert task.average_of_list() == 5.5

def test_largest_element():
    assert task.largest_element() == 10

def test_smallest_element():
    assert task.smallest_element() == 1
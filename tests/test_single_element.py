"""Tests for finding the single element."""

import pytest

from single_element import find_single_element


def test_example_from_exercise():
    assert find_single_element([1, 2, 3, 4, 3, 1, 2]) == 4


def test_single_value_list():
    assert find_single_element([9]) == 9


def test_negative_numbers():
    assert find_single_element([-1, 5, -1, 3, 5]) == 3


def test_zero_as_single_element():
    assert find_single_element([7, 0, 7]) == 0


def test_larger_input():
    assert find_single_element([10, 3, 10, 4, 4, 8, 8, 11, 3]) == 11


def test_even_length_is_invalid():
    with pytest.raises(ValueError):
        find_single_element([1, 1, 2, 2])


def test_multiple_single_elements_are_invalid():
    with pytest.raises(ValueError):
        find_single_element([1, 2, 3])


def test_non_integer_input_is_invalid():
    with pytest.raises(TypeError):
        find_single_element([1, 1, "2"])

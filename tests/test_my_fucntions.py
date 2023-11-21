import source.my_functions as my_functions
import pytest


def test_add():
    result = my_functions.add(num_1=1, num_2=5)

    assert result == 6


def test_divide():
    result = my_functions.divide(num_1=9, num_2=3)

    assert result == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(num_1=1, num_2=0)

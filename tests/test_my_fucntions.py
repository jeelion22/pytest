import source.my_functions as my_functions
import pytest
import time


def test_add():
    result = my_functions.add(num_1=1, num_2=5)

    assert result == 6


def test_divide():
    result = my_functions.divide(num_1=9, num_2=3)

    assert result == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(num_1=1, num_2=0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)

    result = my_functions.divide(num_1=9, num_2=3)

    assert result == 3


@pytest.mark.skip(reason="THis feature is currently broken")
def test_add():
    assert my_functions.add(num_1=1, num_2=3) == 4


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(num_1=4, num_2=0)

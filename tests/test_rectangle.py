import pytest

import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)


def test_area(my_rectangle):
    # reactangle = shapes.Rectangle(10, 20)
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.perimeter() == 2 * 10 + 2 * 20

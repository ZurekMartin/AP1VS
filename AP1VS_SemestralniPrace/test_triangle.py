"""
Semestralni prace z predmetu AP1VS.

Skupina: ST1416
Projekt: Triangle
Autori: Martin Zurek, David Fiala, David Tomecek, Josef Kuzel, David Zidek

Kod slouzici k provedeni unit testu
"""

# Libraries import
from triangle import size_length
from triangle import perimeter
from triangle import area
from triangle import constructability
from triangle import right_angle_check
import pytest


# Test function for calculating the length of the triangle side
def test_size_length():
    assert size_length(2, 2, 9, 2) == 7

    with pytest.raises(TypeError):
        size_length(9 + 10j, 5 + 1j, 5 + 4j, 10 + 8j)
        size_length("v", "p", "r", "g")


# Test function for calculating the perimeter of the triangle
def test_perimeter():
    assert perimeter(7, 5, 4) == 16

    with pytest.raises(TypeError):
        perimeter(2 + 6j, 1 + 4j, 1 + 6j)
        perimeter("o", "g", "a")


# Test function for calculating the area of the triangle
def test_area():
    assert area(8, 3, 6) == 7.644442425710328

    with pytest.raises(TypeError):
        area(1 + 6j, 3 + 9j, 3 + 7j)
        area("m", "r", "k")


# Test function for checking the constructability of the triangle ABC
def test_constructability():
    assert constructability(6, 8, 9) is True
    assert constructability(2, 2, 4) is False

    with pytest.raises(TypeError):
        constructability(9 + 6j, 8 + 2j, 6 + 7j)
        constructability("t", "v", "c")


# Test function for checking the right angle of the triangle ABC
def test_right_angle_check():
    assert right_angle_check(10, 8, 6) is True
    assert right_angle_check(4, 6, 8) is False

    with pytest.raises(TypeError):
        right_angle_check(7 + 1j, 9 + 7j, 10 + 4j)
        right_angle_check("s", "o", "j")

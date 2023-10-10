"""
Závěrečný projekt z předmětu AP1VS.

Skupina: ST1416
Projekt: Trojúhelník
Autoři: Martin Žůrek, David Fiala, David Tomeček, Josef Kužel, David Žídek

Hlavní kód projektu trojúhelník
"""

# Libraries import
import math
import time


# Function for calculating the length of the triangle side
def size_length(first_point_x, first_point_y, second_point_x, second_point_y):
    """
    Calculation of the length of the triangle side.

    :param first_point_x: Input parameter x coordinate of the first point
    :param first_point_y: Input parameter y coordinate of the first point
    :param second_point_x: Input parameter x coordinate of the second point
    :param second_point_y: Input parameter y coordinate of the second point
    :return: Returns the length of the triangle side
    """
    if (type(first_point_x) not in [int, float] or
            type(first_point_y) not in [int, float] or
            type(second_point_x) not in [int, float] or
            type(second_point_y) not in [int, float]):
        raise TypeError()
    else:
        side = math.sqrt(math.pow(first_point_x - second_point_x, 2) +
                         math.pow(first_point_y - second_point_y, 2))
        return side


# Function for calculating the perimeter of the triangle
def perimeter(side_a, side_b, side_c):
    """
    Calculation of the perimeter of the triangle ABC.

    :param side_a: Input parameter size of side a
    :param side_b: Input parameter size of side b
    :param side_c: Input parameter size of side c
    :return: Returns the size of the perimeter of the triangle ABC
    """
    if (type(side_a) not in [int, float] or
            type(side_b) not in [int, float] or
            type(side_c) not in [int, float]):
        raise TypeError()
    else:
        perimeter = side_a + side_b + side_c
        return perimeter


# Function for calculating the area of the triangle
def area(side_a, side_b, side_c):
    """
    Calculation of the area of the triangle ABC.

    :param side_a: Input parameter size of side a
    :param side_b: Input parameter size of side b
    :param side_c: Input parameter size of side c
    s - variable for calculating the semi-perimeter
    :return: Returns the size of the area of the triangle ABC
    """
    if (type(side_a) not in [int, float] or
            type(side_b) not in [int, float] or
            type(side_c) not in [int, float]):
        raise TypeError()
    else:
        s = (side_a + side_b + side_c) / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        return area


# Function for checking the constructability of the triangle
def constructability(side_a, side_b, side_c):
    """
    Checking the constructability of the triangle ABC.

    :param side_a: Input parameter size of side a
    :param side_b: Input parameter size of side b
    :param side_c: Input parameter size of side c
    :return: Returns the value YES or NO
    """
    if (type(side_a) not in [int, float] or
            type(side_b) not in [int, float] or
            type(side_c) not in [int, float]):
        raise TypeError()
    else:
        if ((side_a + side_b > side_c) and
                (side_b + side_c > side_a) and
                (side_c + side_a > side_b)):
            return True
        else:
            return False


# Function for checking the right angle of the triangle
def right_angle_check(side_a, side_b, side_c):
    """
    Checking the right angle of the triangle ABC.

    :param side_a: Input parameter size of side a
    :param side_b: Input parameter size of side b
    :param side_c: Input parameter size of side c
    :return: Returns the value YES or NO
    """
    if (type(side_a) not in [int, float] or
            type(side_b) not in [int, float] or
            type(side_c) not in [int, float]):
        raise TypeError()
    else:
        if ((math.pow(side_a, 2) + math.pow(side_b, 2) ==
             math.pow(side_c, 2)) or
                (math.pow(side_b, 2) + math.pow(side_c, 2) ==
                 math.pow(side_a, 2)) or
                (math.pow(side_c, 2) + math.pow(side_a, 2) ==
                 math.pow(side_b, 2))):
            return True
        else:
            return False


# Function for displaying the properties of the triangle
def triangle(aX, aY, bX, bY, cX, cY):
    # Calling function for calculating the length of the triangle side and perimeter and area
    side_a = size_length(bX, bY, cX, cY)
    side_b = size_length(aX, aY, cX, cY)
    side_c = size_length(aX, aY, bX, bY)
    result_of_function_perimeter = perimeter(side_a, side_b, side_c)
    result_of_function_area = area(side_a, side_b, side_c)

    # Calling function for checking the constructability of the triangle
    if constructability(side_a, side_b, side_c):
        print("Point A = [%.1f, %.1f]" % (aX, aY))
        print("Point B = [%.1f, %.1f]" % (bX, bY))
        print("Point C = [%.1f, %.1f]" % (cX, cY))
        time.sleep(2)
        print()
        print("Length of side a = %.1f cm." % side_a)
        print("Length of side b = %.1f cm." % side_b)
        print("Length of side c = %.1f cm." % side_c)
        time.sleep(2)
        print()
        print("Triangle ABC has perimeter = %.1f cm." % result_of_function_perimeter)
        time.sleep(2)
        print()
        print("Triangle ABC has area = %.1f cm2." % result_of_function_area)
        time.sleep(2)
        print()
        if right_angle_check(side_a, side_b, side_c):
            print("Triangle ABC is right-angled.")
        else:
            print("Triangle ABC is not right-angled.")
        time.sleep(2)
        print()
        print("Triangle ABC can be constructed.")
    else:
        print("Triangle ABC cannot be constructed.")


triangle(2, 5, 2, 2, 9, 2)

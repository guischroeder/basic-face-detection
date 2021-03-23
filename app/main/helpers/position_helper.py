from math import floor


def find_position(value):
    position = floor(value / 100)

    if value % 100 == 0:
        position = position - 1

    return position


def center_of_square(coordinate, dimension):
    return coordinate + dimension / 2

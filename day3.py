# Day 3
# Part 1: Number of valid triangles
# Part 2: Number of valid triangles, split by groups of three numbers by column

from day0 import *


def parse(data):
    """input: byte object
       output: list of lists of numbers"""
    l = list(map(parse_line, data.split('\n')))
    return [el for el in l if el != []]


def parse_line(line):
    """input: string
       output: list of numbers or []"""
    if line.isspace():
        return []
    return list(map(int, line.split()))


def check_triangle(sides):
    """input: list of numbers
       output: bool indicating whether list form valid sides of triangle"""
    print(sides)
    if not len(sides) == 3:
        return False
    sides.sort()
    if int(sides[0]) + int(sides[1]) > int(sides[2]):
        return True
    return False


def num_triangles(data):
    """return number of valid triangles, sides of triangle per row"""
    return sum(list(map(check_triangle, data)))


def num_triangles2(data):
    """count triangles vertically by column in groups of three"""
    data = np.array(data).T.flatten()
    triangles = [data[i:i+3] for i in range(0, len(data), 3)]
    return sum(list(map(check_triangle, triangles)))


if __name__ == "__main__":
    data = parse(Input(3).read())
    print(num_triangles(data))
    print(num_triangles2(data))
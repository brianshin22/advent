# Inspired by Peter Norvig Advent of Code challenge
# Uses Peter Norvig's website to get input files for Advent of Code 2016
import urllib.request
import re

def Input(day):
    """"Open this day's input file."""
    filename = 'input/input{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        raise AssertionError("Input file not found.")


# point is a tuple
def x(point): return point[0]


def y(point): return point[1]


def distance_l1(p1, p2):
    """Manhattan distance between two points"""
    return abs(x(p1) - x(p2)) + abs(y(p1) - y(p2))


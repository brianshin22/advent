# Day 2
# To fix: pad array and check for pad, won't need to check range, same function for both parts

from day0 import *


def part1(data):
    """ run part 1"""
    # Keypad
    # 1 2 3
    # 4 5 6
    # 7 8 9
    keypad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    buttons = 0

    row = 1
    col = 1

    for line in data:
        for char in line:
            nr = row
            nc = col
            if char == 'U':
                nr -= 1
            elif char == 'D':
                nr += 1
            elif char == 'L':
                nc -= 1
            else:
                nc += 1
            if nr in range(0, 3) and nc in range(0, 3):
                row = nr
                col = nc
        buttons = buttons*10 + (keypad[row, col])

    print(buttons)
    return buttons


def part2(data):
    """run part 2"""

    # Keypad
    # 0 0 1 0 0
    # 0 2 3 4 0
    # 5 6 7 8 9
    # 0 A B C 0
    # 0 0 D 0 0
    keypad = np.array([[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]])
    buttons = []

    row = 2
    col = 0

    for line in data:
        for char in line:
            nr = row
            nc = col
            if char == 'U':
                nr -= 1
            elif char == 'D':
                nr += 1
            elif char == 'L':
                nc -= 1
            else:
                nc += 1
            if nr in range(0, len(keypad)) and nc in range(0, len(keypad)):
                if not keypad[nr, nc] == '0':
                    row = nr
                    col = nc
                    print("Row: " + str(row) + " Col: " + str(col))
                    print(keypad[nr, nc])
        buttons.append(keypad[row, col])

    print(buttons)
    return ''.join(buttons)


if __name__ == "__main__":
    data = Input(2).read().split()
    # part1(data)
    print(part2(data))
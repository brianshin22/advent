# Day 5

import hashlib

BIG = 10 ** 999

door = 'ugkcyxxp'

def part1():
    """check for five leading zeros, 6th is password character"""
    password = ''
    for j in range(BIG):
        data = door + str(j)
        #print(data)
        x = hashlib.md5(data.encode('utf-8')).hexdigest()
        #print(x)
        j += 1
        if x.startswith('00000'):
            password += x[5]
            print(j - 1, x, password)
            if len(password) == 8:
                return password


def part2():
    """check for five leading zeros, 6th is index if valid, 7th is password character"""
    password = [None] * 8
    count = 0
    for j in range(BIG):
        data = door + str(j)
        #print(data)
        x = hashlib.md5(data.encode('utf-8')).hexdigest()
        #print(x)
        if x.startswith('00000') and x[5].isdigit():
            index = int(x[5])
            if index in range(0, 8) and password[index] is None:
                password[index] = x[6]
                count += 1
                print(j, x, password)
                if count == 8:
                    return ''.join(password)

print(part1())
#print(part2())


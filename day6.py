# Day 6

from day0 import *


def decode(least_common=False):
    """part 1 find most frequent character in column. part2 find least frequent character"""
    message = []
    data = parse(6)
    transpose = list(np.array([s2a(s) for s in data]).T)

    for line in transpose:
        freqs = collections.Counter(line)

        # part 1: most common letter
        if not least_common:
            tup = freqs.most_common(1)

        # part 2: least common letter
        else:
            tup = freqs.most_common()[-1]
        message.append(tup[0][0])

    return l2s(message)

# part 1
# print(decode())
# part 2
print(decode(True))


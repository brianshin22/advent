# Day 9
# Norvig version

from day0 import *

matcher = re.compile(r'[(](\d+)x(\d+)[)]').match


def decompress(s):
    s = re.sub(r'\s', '', s)
    result = []
    i = 0
    while i < len(s):
        m = matcher(s, i)
        if m:
            i = m.end()
            C, R = map(int, m.groups())
            result.append(s[i:i+C] * R)
            i += C
        else:
            result.append(i)
            i += 1
    return l2s(result)

print(len(decompress(Input(9).read())))

def decompress_length(s):
    s = re.sub(r'\s', '', s)
    length = 0
    i = 0
    while i < len(s):
        m = matcher(s, i)
        if m:
            i = m.end(0)
            C, R = map(int, m.groups())
            length += R * decompress_length(s[i:i+ C])
            i += C
        else:
            length += 1
            i += 1
    return length

print(decompress_length(Input(9).read()))
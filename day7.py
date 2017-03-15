# Day 7
# Peter Norvig version

from day0 import *

# return list of groups separated by whether they are in brackets or not
def segment(s): return re.split(r'\[|\]', s)


# return string of segments outside brackets
def outside(segments): return ', '.join(segments[0::2])


# return string of segments inside brackets
def inside(segments): return ', '.join(segments[1::2])


# check for abba in a string s
def abba(s): return any(a == d != b == c for (a, b, c, d) in subsequences(s, 4))


# return list of all subsequences of string of length n
def subsequences(s, n): return [s[i:i+n] for i in range(len(s) - n + 1)]


# check whether abba outside brackets and not abba in brackets
def tls(segments): return abba(outside(segments)) and not abba(inside(segments))


# check aba outside brackets and bab in brackets for entire alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def ssl(segments):
    return any(a + b + a in outside(segments) and b + a + b in inside(segments) for a in alphabet for b in alphabet if a != b)

print(sum(tls(segment(line)) for line in Input(7)))
print(sum(ssl(segment(line)) for line in Input(7)))
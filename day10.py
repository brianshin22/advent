# Day 10

# from Norvig

from day0 import *

def bots(instructions, goal = {61, 17}):
    def give(giver, value, recip):
        """give value from giver to recip, trigger recip's give if it has two chips"""
        has[giver].discard(value)
        has[recip].add(value)
        chips = has[recip]
        if chips == goal:
            print(recip, 'has', goal)
        if len(chips) == 2:
            give(recip, min(chips), gives[recip][0])
            give(recip, max(chips), gives[recip][1])
    # dictionary of what each bin has (bots, output)
    has = collections.defaultdict(set)
    # dictionary describing giving rules for each robot
    gives = {giver: (dest1, dest2) for (giver, dest1, dest2)
             in re.findall(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', instructions)}
    # trigger initial gives from input
    for (chip, recip) in re.findall(r'value (\d+) goes to (\w+ \d+)', instructions):
        give('input', int(chip), recip)
    return has

has = bots(Input(10).read())
print(has['output 0'].pop() * has['output 1'].pop() * has['output 2'].pop())
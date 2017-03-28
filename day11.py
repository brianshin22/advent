# Day 11
from day0 import *
from heapq import heappop, heappush

# F4
# F3    TM
# F2    TG  RG  RM  CG  CM
# F1 E  SG  SM  PG  PM

"""
Rules:
Must move exactly one or two things per step
destination of M must have its corresponding G if other Gs present at dest, unless they are traveling together
everything must end at F4
"""


def astar_search(start, h_func, neighbors_func):
    """ returns shortest path from start to goal (as defined by heuristic function h_func, and neighbors_func
        which calculates all possible neighbors of a node"""
    frontier = [(h_func(start), start)] # Priority Queue of unexplored nodes, indexed by priority
    previous = {start: None} # dict of where node came from
    cost_so_far = {start: 0} # best total cost to get to state, visited nodes
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0: # heuristic is 0, we've reached goal node
            return Path(previous, s) # return path from start to s
        for next in neighbors_func(s):
            new_cost = cost_so_far[s] + 1 # new calculated cost to get to next from start through s
            if next not in cost_so_far or new_cost < cost_so_far[next]: # this is shortest path
                cost_so_far[next] = new_cost # update shortest path
                heappush(frontier, (new_cost + h_func(next), next)) # add to Priority Queue
                previous[next] = s
    return dict(fail=True, front=len(frontier), prev=len(previous)) # failed to find goal

def Path(previous, s):
    return ([] if (s is None) else Path(previous, previous[s]) + [s])


State = namedtuple('State', 'elevator, floors')

def fs(*items): return frozenset(items)

legal_floors = {0, 1, 2, 3}

def combos(things):
    "All subsets of 1 or 2 things."
    for s in chain(combinations(things, 1), combinations(things, 2)):
        yield fs(*s)

def moves(state):
    "All legal states that can be reached in one move from this state"
    L, floors = state
    for L2 in {L + 1, L - 1} & legal_floors:
        for stuff in combos(floors[L]):
            newfloors = tuple((s | stuff if i == L2 else
                               s - stuff if i == state.elevator else
                               s)
                              for (i, s) in enumerate(state.floors))
            if legal_floor(newfloors[L]) and legal_floor(newfloors[L2]):
                yield State(L2, newfloors)

def legal_floor(floor):
    "Floor is legal if no RTG, or every chip has its corresponding RTG."
    rtgs  = any(r.endswith('G') for r in floor)
    chips = [c for c in floor if c.endswith('M')]
    return not rtgs or all(generator_for(c) in floor for c in chips)

def generator_for(chip): return chip[0] + 'G'

def h_to_top(state):
    "An estimate of the number of moves needed to move everything to top."
    total = sum(len(floor) * i for (i, floor) in enumerate(reversed(state.floors)))
    return math.ceil(total / 2) # Can move two items in one move.


part1 = State(0, (fs('SG', 'SM', 'PG', 'PM'), fs('TG', 'RG', 'RM', 'CG', 'CM'), fs('TM'), fs()))
part2 = State(0, (fs('EG', 'EM', 'DG', 'DM', 'SG', 'SM', 'PG', 'PM'), fs('TG', 'RG', 'RM', 'CG', 'CM'), fs('TM'), fs()))

#path = astar_search(part1, h_to_top, moves)
path = astar_search(part2, h_to_top, moves)
print(len(path) - 1)
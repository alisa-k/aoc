with open('../inputs/day7.txt', 'r') as f:
    positions = [int(x) for x in f.read().strip().split(',')]

def cost(x):
    return sum([abs(x-pos) for pos in positions])

def check(i):
    return cost(i) > cost(i+1)

def solve(positions):
    lo = min(positions)
    hi = max(positions)

    if not check(lo): return cost(lo)
    if check(hi-1): return cost(hi)

    while hi - lo > 1:
        mid = (lo + hi)//2
        if check(mid):
            lo = mid
        else:
            hi = mid
    return cost(hi)

print(solve(positions))

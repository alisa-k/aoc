import heapq 

def solve1():
    lines = parse_input("input.txt")

    max_cals, cur_cals = 0, 0
    for line in lines:
        if line == "\n": # start over
            max_cals = max(max_cals, cur_cals)
            cur_cals = 0
        else:
            cur_cals += int(line.strip())
    return max_cals

def solve2():
    lines = parse_input("input.txt")

    pq = [float('-inf')] * 3
    cur_cals = 0
    for line in lines:
        if line == "\n": # start over
            heapq.heappushpop(pq, cur_cals)
            cur_cals = 0
        else:
            cur_cals += int(line.strip())
    # push the last calorie count
    heapq.heappushpop(pq, cur_cals)
    return sum(pq)

if __name__ == "__main__":
   print(f'Part 1: {solve1()}')
   print(f'Part 2: {solve2()}')

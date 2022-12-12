def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27

def common_item(sets):
    intersection = sets[0].intersection(*sets[1:])
    (letter, ) = intersection
    return letter 

def solve1():
    lines = parse_input("input.txt")

    priority_sum = 0
    for line in lines:
        mid = len(line)//2
        r1 = set(line[:mid])
        r2 = set(line[mid:])
        item = common_item([r1, r2])
        priority_sum += priority(item)
    return priority_sum

def solve2():
    lines = parse_input("input.txt")

    priority_sum = 0
    for i in range(0, len(lines), 3):
        r1 = set(lines[i].strip())
        r2 = set(lines[i+1].strip())
        r3 = set(lines[i+2].strip())
        item = common_item([r1, r2, r3])
        priority_sum += priority(item)
    return priority_sum

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
   print(f'Part 1: {solve1()}')
   print(f'Part 2: {solve2()}')
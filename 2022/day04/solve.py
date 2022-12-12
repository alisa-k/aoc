def assignment(elf):
    lo, hi = [int(c) for c in elf.split("-")]
    return lo, hi

def contains(range1, range2):
    lo1, hi1 = range1
    lo2, hi2 = range2
    return (
        # range 1 contains range 2
        (lo1 <= lo2 and hi2 <= hi1) or 
        # range 2 contains range 1
        (lo2 <= lo1 and hi1 <= hi2))

def overlaps(range1, range2):
    lo1, hi1 = range1
    lo2, hi2 = range2
    return (
        (lo2 <= lo1 <= hi2) or 
        (lo1 <= lo2 <= hi1))

def solve1():    
    lines = parse_input("input.txt")

    count = 0
    for line in lines:
        elf1, elf2 = line.split(",")
        elf1 = assignment(elf1) 
        elf2 = assignment(elf2)
        if contains(elf1, elf2):
            count += 1 
    return count

def solve2():
    lines = parse_input("input.txt")

    count = 0
    for line in lines:
        elf1, elf2 = line.split(",")
        elf1 = assignment(elf1) 
        elf2 = assignment(elf2)
        if overlaps(elf1, elf2):
            count += 1
    return count

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
   print(f'Part 1: {solve1()}')
   print(f'Part 2: {solve2()}')
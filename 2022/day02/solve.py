RPS = {'A': 'R', 'B': 'P', 'C': 'S',
       'X': 'R', 'Y': 'P', 'Z': 'S'}
MOVE_POINTS = {'R': 1, 'P': 2, 'S': 3}

def solve1():
    lines = parse_input("input.txt")

    win_combos = {
        ('R', 'P'), # paper beats rock 
        ('P', 'S'), # scissors beat paper
        ('S', 'R'), # rock beats scissors
    }

    score = 0
    for line in lines:
        op, me = line.split()
        op, me = RPS[op], RPS[me]
        if (op, me) in win_combos: 
            score += 6
        elif me == op: 
            score += 3
        score += MOVE_POINTS[me]
    return score


def solve2():
    lines = parse_input("input.txt")

    result_points = {'X': 0, 'Y': 3, 'Z': 6}
    game_result = {
        'X': {'R': 'S', 'P': 'R', 'S': 'P'}, # lose
        'Y': {'R': 'R', 'P': 'P', 'S': 'S'}, # draw
        'Z': {'R': 'P', 'P': 'S', 'S': 'R'}, # win
    }

    score = 0
    for line in lines:
        op, res = line.split()
        op_move = RPS[op] # map ABC to RPS
        my_move = game_result[res][op_move]
        score += result_points[res]
        score += MOVE_POINTS[my_move]
    return score

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
   print(f'Part 1: {solve1()}')
   print(f'Part 2: {solve2()}')
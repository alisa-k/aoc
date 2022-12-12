def parse_input():
	with open("input.txt", "r") as f:
		lines = f.readlines()

	# start from last line and read instructions
	instructions = []
	# iterator representing line number 
	# we're currently on
	current = 0 
	for i in range(len(lines)-1, -1, -1):
		if lines[i] == "\n":
			current = i-1
			break
		parts = lines[i].split()
		instructions.append(
			(int(parts[1]), 
			 int(parts[3]), 
			 int(parts[5])))
	# get instructions in reverse (correct) order
	instructions = instructions[::-1]
	# find number of columns using current line index
	# and finding the last number in that line
	num_cols = int(lines[current].strip().split()[-1])

	# get the initial state of the stacks 1 through num_cols 
	stacks = {k + 1: [] for k in range(num_cols)}
	for i in range(start-1, -1, -1):
		line = lines[i]
		row = [line[j:j+4].strip() for j in range(0, num_cols*4, 4)]
		for j in range(len(row)):
			if not row[j]: continue
			stacks[j+1].append(row[j])
	return instructions, stacks

def solve1():
	instructions, stacks = parse_input()
	# follow instructions
	for instruction in instructions:
		num, cur, nxt = instruction
		for i in range(num):
			item = stacks[cur].pop()
			stacks[nxt].append(item)
	
	# find tops of stacks
	message = ""
	for i in range(len(stacks)):
		message += stacks[i+1][-1][1]

	return message


def solve2():
	instructions, stacks = parse_input()
	# follow instructions
	for instruction in instructions:
		num, cur, nxt = instruction
		popped_items = []
		for i in range(num):
			popped_items.append(stacks[cur].pop())
		stacks[nxt].extend(popped_items[::-1])

	# find tops of stacks
	message = ""
	for i in range(len(stacks)):
		message += stacks[i+1][-1][1]

	return message

if __name__ == "__main__":
	print(f'Part 1: {solve1()}')
	print(f'Part 2: {solve2()}')
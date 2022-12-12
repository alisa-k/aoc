import math

def lcm(nums):
  product = math.prod(nums)
  gcd = math.gcd(nums[0], nums[1])
  for num in nums[2:]:
  	gcd = math.gcd(gcd, num)
  return product // gcd 

def parse_input():
	with open("input.txt", "r") as f: 
		lines = f.readlines()
	monkey_items = []
	monkey_business = []
	worries = []
	i = 0
	while i < len(lines):
		if lines[i].startswith("Monkey"):
			items = [int(item) for item in lines[i + 1].strip().split(":")[-1].split(", ")]
			operation = lines[i + 2].strip().split(":")[1].strip().split(" = old ")[-1]
			d =  int(lines[i + 3].strip().split(" ")[-1])
			m1 = int(lines[i + 4].strip().split(" ")[-1])
			m2 = int(lines[i + 5].strip().split(" ")[-1])
			monkey_items.append(items)
			monkey_business.append([operation, (d, m1, m2)])
			worries.append(d)
		i += 1
	return monkey_items, monkey_business, worries

def get_new_item(item, operation):
	op, mag = operation.split(" ")
	new_item = item
	if mag == "old": new_item *= new_item
	elif op == "+": new_item += int(mag) 
	elif op == "*": new_item *= int(mag)
	return new_item

def solve(num_rounds, part):
	monkey_items, monkey_business, worries = parse_input()
	num_monkeys = len(monkey_items)
	inspection_count = [0] * num_monkeys

	for round_number in range(num_rounds):
		new_monkey_items = [list(monkey_items[m]) for m in range(num_monkeys)]
		for m in range(num_monkeys):
			# monkey m's turn
			operation, test = monkey_business[m]
			op, mag = operation.split(" ")
			div, m1, m2 = test
			items = monkey_items[m]
			for i, item in enumerate(items):
				# inspect item
				inspection_count[m] += 1
				# get new item value
				new_item = get_new_item(item, operation)
				# reduce worry
				if part == "part1":
					new_item //= 3
				else:
					new_item %= lcm(worries)
				# remove the item from current monkey list
				new_monkey_items[m].pop(0)
				# pass the item to the next monkey based on test
				next_monkey = m1 if new_item % div == 0 else m2
				new_monkey_items[next_monkey].append(new_item)
			monkey_items = [list(new_monkey_items[m]) for m in range(num_monkeys)]

	# get max 2 inspection counts & return 
	inspections = sorted(inspection_count)
	return inspections[-1] * inspections[-2]

def solve1():
	return solve(20, "part1")

def solve2():
	return solve(10000, "part2")

if __name__ == "__main__":
	print(f'Part 1: {solve1()}')
	print(f'Part 2: {solve2()}')
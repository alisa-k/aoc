def parse_input():
	with open("input.txt", "r") as f:
		lines = f.readlines()
	return lines 

def first_unique_k_window(k):
	s = parse_input()[0]
	last_seen_idx = {}
	start = end = 0
	while end < len(s):
		c = s[end]
		if c in last_seen_idx and last_seen_idx[c] >= start:
			start = last_seen_idx[c] + 1
		last_seen_idx[c] = end
		# current window size is length k
		if end - start + 1 == k:
			return start, end
		end += 1
	return start, end

def solve1():
	start, end = first_unique_k_window(4)
	return end + 1
	

def solve2():
	start, end = first_unique_k_window(14)
	return end + 1

if __name__ == "__main__":
	print(f'Part 1: {solve1()}')
	print(f'Part 2: {solve2()}')
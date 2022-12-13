from collections import deque 

def transform(c):
	if c == 'S': return 0
	if c == 'E': return 27
	return ord(c) - ord('a') + 1

def parse_input():
	with open("input.txt", "r") as f: 
		lines = f.readlines()
	grid = [[transform(c) for c in line.strip()] for line in lines]
	return grid

def solve(grid, start, end):
	m, n = len(grid), len(grid[0])
	
	def valid_neighbors(r, c):
		directions = [(-1,0), (0,-1), (1,0), (0,1)]
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			in_bounds = 0 <= nr < m and 0 <= nc < n
			if not in_bounds: continue
			can_move = grid[nr][nc] <= grid[r][c] + 1
			if not can_move: continue
			unvisited = (nr, nc) not in visited
			if not unvisited: continue
			yield nr, nc

	visited = set([start])
	queue = deque([start])
	steps = 0
	while queue:
		steps += 1
		for j in range(len(queue)):
			r, c = queue.popleft()
			for nei in valid_neighbors(r, c):
				if nei == end: return steps
				visited.add(nei)
				queue.append(nei)
	# target unreachable from source
	return float('inf')

def solve1(grid, m, n):
	start = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 0][0]
	end = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 27][0]
	return solve(grid, start, end)

def solve2(grid, m, n):
	starts = [(r, c) for r in range(m) for c in range(n) if grid[r][c] <= 1]
	end = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 27][0]
	return min([solve(grid, start, end) for start in starts])

if __name__ == "__main__":
	grid = parse_input()
	m, n = len(grid), len(grid[0])
	print(f'Part 1: {solve1(grid, m, n)}')
	print(f'Part 2: {solve2(grid, m, n)}')
from collections import deque 

def parse_input():
	with open("input.txt", "r") as f: 
		lines = f.readlines()
	grid = []
	for line in lines:
		grid.append(list(line.strip()))
	start = end = None
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 'S':
				start = (i, j)
				grid[i][j] = 0
			elif grid[i][j] == 'E':
				end = (i, j)
				grid[i][j] = 27
			else:
				grid[i][j] = ord(grid[i][j]) - ord('a') + 1
	return grid, start, end

def solve1():
	grid, start, end = parse_input()
	m, n = len(grid), len(grid[0])

	def valid_neighbors(r, c):
		directions = [(-1,0), (0,-1), (1,0), (0,1)]
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			can_move = (
				0 <= nr < m and 0 <= nc < n and 
				grid[nr][nc] <= grid[r][c] + 1 and
				(nr, nc) not in visited)
			if can_move: 
				yield nr, nc

	visited = set([start])
	queue = deque([start])
	steps = 0
	while queue:
		steps += 1
		for j in range(len(queue)):
			r, c = queue.popleft()
			for nr, nc in valid_neighbors(r, c):
				if (nr, nc) == end: 
					return steps
				visited.add((nr, nc))
				queue.append((nr, nc))
	return steps

def solve2():
	pass

if __name__ == "__main__":
	print(f'Part 1: {solve1()}')
	# print(f'Part 2: {solve2()}')
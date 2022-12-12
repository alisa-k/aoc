def parse_input():
	with open("input.txt", "r") as f:
		lines = f.readlines()
	matrix = []
	for line in lines:
		matrix.append([int(c) for c in line.strip()])
	return matrix

def solve1():
	matrix = parse_input()
	m, n = len(matrix), len(matrix[0])
	
	l = [[matrix[r][c] for c in range(n)] for r in range(m)]
	r = [[matrix[r][c] for c in range(n)] for r in range(m)]
	u = [[matrix[r][c] for c in range(n)] for r in range(m)]
	d = [[matrix[r][c] for c in range(n)] for r in range(m)]
	for i in range(1, m-1):
		for j in range(1, n-1):
			l[i][j] = max(l[i][j-1], matrix[i][j-1])
			u[i][j] = max(u[i-1][j], matrix[i-1][j])
	for i in range(m-2, 0, -1):
		for j in range(n-2, 0, -1):
			r[i][j] = max(r[i][j+1], matrix[i][j+1])
			d[i][j] = max(d[i+1][j], matrix[i+1][j])
	
	visible = m * 2 + n * 2 - 4
	for i in range(1, m-1):
		for j in range(1, n-1):
			min_boundary = min(l[i][j], r[i][j], u[i][j], d[i][j])
			if matrix[i][j] > min_boundary: visible += 1
	return visible

def solve2():
	matrix = parse_input()
	m, n = len(matrix), len(matrix[0])

	# left distances
	l = [view_distance(row) for row in matrix]
	# right distances 
	r = [view_distance(row[::-1])[::-1] for row in matrix]
	# up distances 
	u = [[-1 for c in range(n)] for r in range(m)]
	for j in range(n):
		# make an array out of the jth column
		row = [matrix[i][j] for i in range(m)]
		dists = view_distance(row)
		for i in range(m): u[i][j] = dists[i]
	# down distances
	d = [[-1 for c in range(n)] for r in range(m)]
	for j in range(n):
		# make an array out of the jth column
		row = [matrix[i][j] for i in range(m)]
		dists = view_distance(row[::-1])[::-1]
		for i in range(m): d[i][j] = dists[i]

	# calculate max scenic score
	max_score = 0
	for i in range(m):
		for j in range(n):
			scenic_score = l[i][j] * r[i][j] * u[i][j] * d[i][j]
			max_score = max(max_score, scenic_score)
	return max_score

def view_distance(arr):
	distances = [0]
	stack = [0]
	for i in range(1, len(arr)):
		# maintain stack of decreasing order
		while stack and arr[stack[-1]] < arr[i]:
			stack.pop()
		# view distance is i if this is the largest element seen so far
		# otherwise, view distance is distance between last largest seen
		view_distance = i if not stack else i - stack[-1]
		distances.append(view_distance)
		stack.append(i)
	return distances

if __name__ == "__main__":
	print(f'Part 1: {solve1()}')
	print(f'Part 2: {solve2()}')
def dfs(arr):
	stack = []
	visited = [[False]*len(arr[0]) for i in range(len(arr))]
	stack.append((0,0))
	res = []
	
	while stack:
		row, col = stack.pop()
		if row < 0 or col < 0 or row > len(arr)-1 \
		or col > len(arr)-1 or visited[row][col] == True:
			continue
		
		res.append(arr[row][col])
		visited[row][col] = True
		stack.append((row, col-1))
		stack.append((row, col+1))
		stack.append((row-1, col))
		stack.append((row+1, col))
		
	return res
	

def dfs_recursion(arr):
	visited = [[False] * len(arr[0]) for _ in range(len(arr))]
	res = []
	helper(arr, 0, 0, visited, res)
	return res

def helper(arr, row, col, visited, res):
	
	if row < 0 or col < 0 or row > len(arr)-1 or col > len(arr[0])-1 or visited[row][col] == True:
		return
		
	res.append(arr[row][col])
	visited[row][col] = True
	
	helper(arr, row, col-1, visited, res)
	helper(arr, row, col+1, visited, res)
	helper(arr, row-1, col, visited, res)
	helper(arr, row+1, col, visited, res)
	
	
def bfs(arr):
	queue = []
	queue.append((0,0))
	visited = [[False]*len(arr[0]) for i in range(len(arr))]
	res = []
	
	while queue:
		row, col = queue.pop(0)
		
		if row < 0 or col < 0 or row > len(arr)-1 or col > len(arr[0])-1 or visited[row][col] == True:
			continue
		
		res.append(arr[row][col])
		visited[row][col] = True
		
		queue.append((row, col-1))
		queue.append((row, col+1))
		queue.append((row-1, col))
		queue.append((row+1, col))
		
	return res

def bfs_recursion(arr):
	visited = [[False]*len(arr[0]) for i in range(len(arr))]
	res = []
	
	helper_bfs(arr, 0, 0, visited, res)

def helper_bfs(arr, row, col, visited, res):
	if row < 0 or col < 0 or row > len(arr)-1 or col > len(arr[0])-1 or visited[row][col]
		
if __name__ == '__main__':
	arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
	
	res = dfs_recursion(arr)
	print(res)
	
	res = bfs(arr)
	print(res)
	
		
		
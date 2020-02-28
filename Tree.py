def preorder(root):
	res = []
	stack = []
	cur = root
	
	while cur is not None or len(stack) != 0:
		if cur is not None:
			res.append(cur.val)
			stack.append(cur)
			cur = cur.left
		else:
			cur = stack.pop().right
	return res	
	
	
def inorder(root):
	res = []
	stack = []
	cur = root
	
	while cur is not None or len(stack) != 0:
		if cur is not None:
			stack.append(cur)
			cur = cur.left
		else:
			temp = stack.pop()
			res.append(temp)
			cur = temp.right
			

def postorder(root):
	if root is None:
		return root
	stack = []
	stack.append(root)
	visited = root
	
	while len(stack) != 0:
		temp = stack.pop()
		if (temp.left is None and temp.right is None) or (temp.left is visited or temp.left is visited):
			res.append(temp)
			visited = temp
		else:
			stack.append(temp)
			if temp.right is not None: stack.append(temp.right)
			if temp.left is not None: stack.append(temp.left)
	return res

			
def levelorder(root):
	if root is None: 
		return root
	res = []
	queue = []
	queue.append(root)
	
	while len(queue) != 0:
		temp = queue.pop(0)
		res.append(temp)
		if temp.left is not None:
			res.append(temp.left)
		if temp.right is not None:
			res.append(temp.right)
		
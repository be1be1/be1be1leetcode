class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def levelorder(root:TreeNode):
	queue = []
	queue.append(root)
	res = []
	
	while len(queue) != 0:
		size = len(queue)
		for i in range(size):
			cur = queue.pop(0)
			if cur.left:
				queue.append(cur.left)
			if cur.right:
				queue.append(cur.right)
			if i == 0:
				res.append(cur.val)
				
	return res
	

if __name__ == "__main__":
	l = []
	for i in range(5):
		l.append(TreeNode(i))
	
	l[0].left = l[1]
	l[0].right = l[2]
	l[1].left = l[3]
	l[1].right = l[4]
	
	res = levelorder(l[0])
	
	print(res)
		
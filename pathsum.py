class Solution:
	def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
		if not root:
			return []
		stack = []
		stack.append((root, sum-root.val, [root.val]))
		visited = root
		res = []
		
		while len(stack) != 0:
			temp, val, l = stack.pop()
			
			if (temp.left is None and temp.right is None) or (temp.left is visited or temp.right is visited):
				visited = temp
				if temp.left is None and temp.right is None and val == 0:
					res.append(l)
			else:
				stack.append((temp, val, l))
				if temp.right:
					stack.append((temp.right, val-temp.right.val, l+[temp.right.val]))
				if temp.left:
					stack.append((temp.left, val-temp.left.val, l+[temp.left.val]))
					
		return res
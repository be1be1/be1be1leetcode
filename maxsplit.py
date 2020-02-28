class Solution:
	def maxProduct(self, root: TreeNode) -> int:
		stack = []
		stack.append(root)
		res = []
		visited = root
		max_product = -float('inf')
		
		while len(stack) != 0:
			temp = stack.pop()
			
			if (temp.left is None and temp.right is None) \
			or (temp.left is visited or temp.right is visited):
				visited = temp
				if temp.left is not None:
					temp.val += temp.left.val
				if temp.right is not None:
					temp.val += temp.right.val
				res.append(temp.val)
			else:
				stack.append(temp)
				if temp.right is not None: stack.append(temp.right)
				if temp.left is not None: stack.append(temp.left)
					
		total = res[-1]
		max_product = max(x*(total-x) for x in res) % (10**9+7) 
		
		return max_product % (10**9 + 7)
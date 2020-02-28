def findMinMax(l:list)->list:
	minRight = []
	res = []
	for i in range(len(l)):
		minRight.append(min(l[i:]))
	print(minRight)
	
	cur = l[0]
	for i in range(len(l)):
		if cur < l[i]:
			cur = l[i]
		if cur == minRight[i]:
			res.append(cur)
	return res
	
if __name__ == "__main__":
	l = [7, 10, 2, 6, 19, 22, 32]
	print(findMinMax(l))
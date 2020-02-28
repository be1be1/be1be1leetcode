def findFeq(arr):
	i = 0
	while i < len(arr):
		tmp = arr[i] - 1
		if tmp < 0:
			i += 1
			continue
		if arr[tmp] > 0:
			arr[i] = arr[tmp]
			arr[tmp] = -1
		else:
			arr[tmp] -= 1
			arr[i] = 0
		print(i)
		print(arr)

	return [abs(i) for i in arr]

if __name__ == "__main__":
	res = findFeq([2, 5, 5, 2, 3])
	print(res)
		
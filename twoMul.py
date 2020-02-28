def twoMul(nums, target):
		nums_dict = {val: idx for idx, val in enumerate(nums)}
		result = []
		for i, j in enumerate(nums):
			if target/j in nums_dict and i != nums_dict[target/j] and i < nums_dict[target/j]:
				result.append([j, target//j])
		return result


if __name__ == '__main__':
	nums = [1,2,4,5,7,8,11,12,15]
	target = 60
	result = twoMul(nums, target)
	if len(result) != 0:
		print(result)
	else:
		print([-1,-1])
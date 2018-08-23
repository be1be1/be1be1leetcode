class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for idx, num in enumerate(nums):
        	if target - num in lookup:
        		return [lookup[target - num], idx]
        	else:
        		lookup[num] = idx
            
if __name__ == '__main__':
	print(Solution().two_sum([2, 7, 11, 15], 9))



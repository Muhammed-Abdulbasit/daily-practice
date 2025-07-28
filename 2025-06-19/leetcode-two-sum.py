class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevList = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevList:
                return(prevList[diff], i)
            prevList[n] = i
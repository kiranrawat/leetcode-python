class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = nums[0]
        result = []
        result.insert(0, sums)
        for i in range(0, len(nums)-1):
            sums = sums + nums[i+1]
            result.append(sums)
        return result  
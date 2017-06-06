class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here

        nums.sort()
        result = 0

        for x in nums:
        	if x % 2 != 0:
        		result = result + x

        return result


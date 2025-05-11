class Solution(object):
    def singleNumber(self, nums):
        single=nums[0]
        for i in range(1,len(nums)):
            single ^= nums[i]
        return single
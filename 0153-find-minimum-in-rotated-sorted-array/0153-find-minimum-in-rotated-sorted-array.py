class Solution(object):
    def findMin(self, nums):
        start,end=0,len(nums)-1
        if nums[end]>nums[start]:
            return nums[start]
        while start<=end:
            mid=(start+end)//2
            #found:
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            #right:
            if nums[mid]>nums[end]:
                start=mid+1
            #left
            else :
                end=mid-1
        return nums[0]
        
        
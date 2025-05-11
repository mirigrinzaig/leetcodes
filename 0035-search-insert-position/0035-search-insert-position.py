class Solution(object):
    def searchInsert(self, nums, target):
        start,end=0,len(nums)-1
        if nums[0]>target:
            return 0
        if nums[end]<target:
            return end+1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target and nums[mid-1]<target:
                return mid
            #search left:
            if nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
           
                
        
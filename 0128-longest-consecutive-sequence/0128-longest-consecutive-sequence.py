# class Solution(object):
#     def longestConsecutive(self, nums):
#         seen = {}
#         longest=0
#         for num in nums:
#             if(num+1)in seen and(num-1) in seen:
#                 seen[num]=seen[num+1]+seen[num-1]+1
#                 longest=max(longest,seen[num])
#                 continue
#             if (num-1) in seen:
#                 seen[num]=seen[num-1]+1
#                 longest=max(longest,seen[num])
#                 continue
#             if(num+1) in seen:
#                 seen[num]=seen[num+1]+1
#                 longest=max(longest,seen[num])
#                 continue
#             else:
#                 seen[num]=1
#         return longest
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest
        
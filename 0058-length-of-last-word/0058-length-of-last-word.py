class Solution(object):
    def lengthOfLastWord(self, s):
        length=0
        # for ch in s:
        #     if ch==" ":
        #         return length
        #     length=length+1
        # return length
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])
        
class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        return string==string[::-1]
        
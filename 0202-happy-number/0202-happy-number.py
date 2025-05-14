         
class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum_digit = 0
            while n > 0:
                digit = n % 10
                sum_digit += digit * digit
                n //= 10
            n = sum_digit
        return True
         
        
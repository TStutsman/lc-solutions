from math import log10

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        
        digits = int(log10(x)) # 6: 0,
        big_divisor = 10 ** digits # 0: 1
        big_end = x // big_divisor # 6/1: 6
        small_end = x % 10 # 767: 7

        if small_end != big_end:
            return False

        right = x % big_divisor # 77%10: 7
        middle = right // 10 # 77 // 10: 7
        return self.isPalindrome(middle)

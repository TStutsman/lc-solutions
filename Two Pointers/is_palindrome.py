class Solution:
    def isPalindrome(self, s: str) -> bool:
        # for first n/2 char, compare if the n-i index char is the same
        n = len(s)
        j = n-1
        for i in range(n//2):
            if not s[i].isalnum():
                continue
            
            while not s[j].isalnum():
                j -= 1

            if s[i].casefold() != s[j].casefold():
                return False
            
            j -= 1
        
        return True
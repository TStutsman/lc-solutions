class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Variable sliding window
        # Conditions for sliding from left
        # - If we encounter the left-most character on the right
        # - -> Move left pointer to next critical character

        # hash map
        # count of characters
        def has_characters(count_hash, target_hash):
            for char in target_hash.keys():
                if count_hash.get(char, 0) < target_hash.get(char, 0):
                    return False
            return True
        
        counts = {}
        target = {}
        min_string = ''

        for char in t:
            target[char] = target.get(char, 0) + 1

        l, r = 0, 0
        while(r < len(s)):
            # add right characters until substring has all characters
            counts[s[r]] = counts.get(s[r], 0) + 1

            # remove left character until substring misses a character
            while has_characters(counts, target):
                if len(min_string) > r - l or len(min_string) == 0:
                    min_string = s[l:r+1]
                
                counts[s[l]] -= 1
                l += 1
            
            r += 1
        
        return min_string
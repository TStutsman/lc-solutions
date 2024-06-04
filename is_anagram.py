class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force O(nlogn)
        # sort both strings alphabetically O(nlogn)
        # iterate over sorted strings: O(n)
        #   return false if characters at index don't match
        # return true if all characters matched

        # 2 O(n)
        # store character counts in hash O(n)
        # iterate over str1 and add chars/increment counts
        # iterate over str2 and decrement counts/remove chars
            # if counts hash doesn't have count/key return false
        # if counts hash still has keys return false
        # if no remaining keys in counts hash return true (exact match)

        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char not in count:
                return False
            elif count[char] > 1:
                count[char] -= 1
            else:
                del count[char]
        
        return len(count) == 0
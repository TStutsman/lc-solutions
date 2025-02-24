class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep a count of all letters
        # left and right pointers
        # longest length variable
        # total char count
        # max_char

        # move right pointer and add letter at right to count
        # when total minus the max char is greater than k
        # move the left pointer and decrement until equal to k

        count = {}
        left = 0
        longest = 0
        max_letter = s[0]

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            
            if count[s[right]] >= count[max_letter]:
                max_letter = s[right]

            while right - left + 1 > count[max_letter] + k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest
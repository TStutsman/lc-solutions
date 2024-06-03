class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a window set to store unique characters
        # create a left and right pointer to keep track of the index of substring
        # create a longest variable that stores the highest substring length

        # increment right until right points to repeat character
            # save each char to window along the way
        # save to max if length is greater than max
        # increment left and remove chars from window until repeat character is removed
        
        # when right reaches the end of the string, return longest

        window = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            curr_char = s[right]

            while curr_char in window:
                window.discard(s[left])
                left += 1
            
            window.add(curr_char)

            longest = max(right-left+1, longest)

        return longest
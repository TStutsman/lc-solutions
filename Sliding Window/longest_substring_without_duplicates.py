# from collections import deque

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # keep a queue and a set
#         # for every character, check if in the set
#             # if so remove first character from queue and set
#             # until set no longer has character
#             # lastly, check if greater than longest and replace if longer

#         # O(n) time | O(n) space

#         longest = 0
#         queue = deque([])
#         unique = set()

#         for char in s:
#             while char in unique:
#                 removed = queue.popleft()
#                 unique.remove(removed)
            
#             unique.add(char)
#             queue.append(char)
#             longest = max(longest, len(queue))
        
#         return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a left pointer and a set
        # for every index, check if character at that index is in the set
            # if so remove character at left pointer from the unique set until the set doesn't have the character
            # lastly, check if current substring greater than longest and replace if longer

        # O(n) time | O(n) space

        longest = 0
        left = 0
        unique = set()

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            
            unique.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest
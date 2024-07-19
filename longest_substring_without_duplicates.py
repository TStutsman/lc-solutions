from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a queue and a set
        # for every character, check if in the set
            # if so remove first character from queue and set
            # until set no longer has character
            # lastly, check if greater than longest and replace if longer

        # O(n) time | O(n) space

        longest = 0
        queue = deque([])
        unique = set()

        for char in s:
            while char in unique:
                removed = queue.popleft()
                unique.remove(removed)
            
            unique.add(char)
            queue.append(char)
            longest = max(longest, len(queue))
        
        return longest
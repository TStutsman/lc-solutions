        # left and right pointers pointing to start, end indeces of string s
        # check if we have visited left,right already
        # check if substring[left:right] is palindrome
        # if it is, it is the longest possible palindrome, so return it
        # if not:
        # add left,right to visited
        # increment left and recur
        # decrement right and recur

        # def is_palindrome(substring):
        #     if len(substring) < 2: return True

        #     half_length = len(substring)//2 + 1
        #     for idx in range(half_length):
        #         if substring[idx] != substring[-1 - idx]:
        #             return False
            
        #     return True

        # visited = set()
        # left, right = 0, len(s)
        
        # def recursively_check_substrings(left, right, longest):
        #     # if we already visited don't check or recur
        #     if (left, right) in visited or left >= right: return
            
        #     visited.add((left,right))
        #     substring = s[left:right]

        #     if is_palindrome(substring):
        #         longest = max(right - left, longest)

        #     recursively_check_substrings(left + 1, right, longest)
        #     recursively_check_substrings(left, right - 1, longest)

        # recursively_check_substrings(left, right, 1)

    # Failed to Timeout

    # Failed due to TIMEOUT ----------
    # Helper function to check for palindromes
    # def _is_palindrome(substring):
    #     if len(substring) < 2: return True

    #     half_length = len(substring)//2 + 1
    #     for idx in range(half_length):
    #         if substring[idx] != substring[-1 - idx]:
    #             return False
        
    #     return True

    # longest = s[0]
    # for left in range(len(s)):
    #     for right in range(1, len(s)+1):
    #         substring = s[left:right]
    #         if _is_palindrome(substring) and right - left > len(longest):
    #             longest = substring

    # return longest

# bfs search for palindrome
# start with queue consisting of string s
# popleft from queue and that is the current substring
# check if we have visited substring already, if so not a palindrome
# if not, check if substring is palindrome
# if it is, it is the longest possible palindrome, so return it
# if not:
# add substring without right character/left character to the queue
from collections import deque

def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    def is_palindrome(substring):
        if len(substring) < 2: return True

        half_length = len(substring)//2 + 1
        for idx in range(half_length):
            if substring[idx] != substring[-1 - idx]:
                return False
        
        return True

    visited = set()
    queue = deque([s])
    
    def substring_bfs(queue):
        while len(queue) > 0:
            substring = queue.popleft()

            # if we already visited don't check
            if substring in visited: continue

            # the first palindrome we visit will be the largest
            if is_palindrome(substring):
                return substring

            # add substring to visited set so we don't check for palindrome again
            visited.add(substring)

            # add left and right substrings to the queue
            left_substring = substring[:-1]
            queue.append(left_substring)
            right_substring = substring[1:]
            queue.append(right_substring)

    return substring_bfs(queue)
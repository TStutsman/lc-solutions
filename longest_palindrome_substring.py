# left and right pointers pointing to start, end indeces of string s
        # check if we have visited left,right already
        # check if substring[left:right] is palindrome
        # if it is compare to longest and save maximum
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
        #     if (left, right) in visited: return
            
        #     visited.add((left,right))
        #     substring = s[left:right]

        #     if is_palindrome(substring):
        #         longest = max(right - left, longest)

        #     recursively_check_substrings(left + 1, right, longest)
        #     recursively_check_substrings(left, right - 1, longest)

        # recursively_check_substrings(left, right, 1)

    # ^^^^^ MAX STACK DEPTH EXCEEDED
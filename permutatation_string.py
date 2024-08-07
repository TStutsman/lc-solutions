# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         # for s1, count all the characters
#         # store counts in a hash -> char: count
#         # for s2, subtract each char from count in hash
#         # if count is zero delete key
#         # if no keys remain, return true
#         # if keys remain after s2 return false

#         counts = {}
#         for c in s1:
#             counts[c] = counts.get(c, 0) + 1
        
#         for c in s2:
#             if c not in counts:
#                 continue

#             if counts[c] < 2:
#                 del counts[c]
#             else:
#                 counts[c] -= 1

#             if len(counts) < 1:
#                 return True

#         return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         # make counts hash of s1
#         # left, right pointers for window in s2
#         # if counts of s2 matches counts of s1 return true
#         # increment left and right
#         # add char at right pointer, remove char from left pointer
#         if len(s1) > len(s2):
#             return False

#         char_count = {}
#         for char in s1:
#             char_count[char] = char_count.get(char, 0) + 1
        
#         for idx in range(len(s1)):
#             if char_count.get(s2[idx]) == 1:
#                 del char_count[s2[idx]]
#             else:
#                 char_count[s2[idx]] = char_count.get(s2[idx], 0) - 1
        
#         r = len(s1)
#         for l in range(len(s2) - len(s1)):
#             print(char_count)
#             if len(char_count) < 1:
#                 return True

#             if char_count.get(s2[l]) == -1:
#                 del char_count[s2[l]]
#             else:
#                 char_count[s2[l]] = char_count.get(s2[l], 0) + 1

#             if char_count.get(s2[r]) == 1:
#                 del char_count[s2[r]]
#             else:
#                 char_count[s2[r]] = char_count.get(s2[r], 0) - 1
            
#             r += 1
        
#         if len(char_count) < 1:
#                 return True
        
#         return False

class Solution:
    def remove_left(self, char_count, left):
        if char_count.get(left) == -1:
                del char_count[left]
        else:
            char_count[left] = char_count.get(left, 0) + 1

    def add_right(self, char_count, right):
        if char_count.get(right) == 1:
                del char_count[right]
        else:
            char_count[right] = char_count.get(right, 0) - 1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make counts hash of s1
        # left, right pointers for window in s2
        # if counts of s2 matches counts of s1 return true
        # increment left and right
        # add char at right pointer, remove char from left pointer
        if len(s1) > len(s2):
            return False

        char_count = {}
        for char in s1:
            char_count[char] = char_count.get(char, 0) + 1
        
        for r in range(len(s1)):
            self.add_right(char_count, s2[r])
            
        if len(char_count) < 1:
                return True

        r = len(s1)
        for l in range(len(s2) - len(s1)):
            self.remove_left(char_count, s2[l])
            self.add_right(char_count, s2[r])
            
            if len(char_count) < 1:
                return True

            r += 1
        
        return False
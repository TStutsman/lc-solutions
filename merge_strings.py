# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         merge_tuples = list(zip(word1, word2))
#         print(merge_tuples)
#         list_format = "".join(list(sum(merge_tuples, ())))

#         remaining = ""
#         if len(word1) > len(word2):
#             remaining = word1[len(word2):]
#         elif len(word2) > len(word1):
#             remaining = word2[len(word1):]

#         return list_format + remaining

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # iterate through the longest of the two
        # at each index, add character from word1, then character from word2
        # if no word1, skip, and viceversa
        # O(n) where n is the number of characters in the longer string

        longest = max(len(word1), len(word2))

        merged = ''
        for i in range(longest):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]

        return merged
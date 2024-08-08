class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_tuples = list(zip(word1, word2))
        print(merge_tuples)
        list_format = "".join(list(sum(merge_tuples, ())))

        remaining = ""
        if len(word1) > len(word2):
            remaining = word1[len(word2):]
        elif len(word2) > len(word1):
            remaining = word2[len(word1):]

        return list_format + remaining
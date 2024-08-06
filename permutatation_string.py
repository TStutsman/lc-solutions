class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for s1, count all the characters
        # store counts in a hash -> char: count
        # for s2, subtract each char from count in hash
        # if count is zero delete key
        # if no keys remain, return true
        # if keys remain after s2 return false

        counts = {}
        for c in s1:
            counts[c] = counts.get(c, 0) + 1
        
        for c in s2:
            if c not in counts:
                continue

            if counts[c] < 2:
                del counts[c]
            else:
                counts[c] -= 1

            if len(counts) < 1:
                return True

        return False
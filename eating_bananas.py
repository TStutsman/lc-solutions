# from math import ceil

# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         # if h is length of piles then k is max of piles
#         # start with k = max O(n)
        
#         # ceil(pile / k )= pile-hours
#         low, high, k = 0, max(piles) * 2, max(piles)
#         check = h + 1
#         while check != h - 1:
#             check = 0
#             k = (high + low) // 2
#             for pile in piles:
#                 check += ceil(pile/k)
            
#             if check > h - 1:
#                 high = k
#             elif check < h - 1:
#                 low = k
        
#         # now k gives h-1
#         while check < h:
#             k += 1
#             check = 0
#             for pile in piles:
#                 check += ceil(pile/k)
        
#         return k

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # if h is length of piles then k is max of piles
        # start with k = min O(n)
        def hours_to_eat(piles: list[int], rate: int):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            
            return hours
        
        # ceil(pile / k )= pile-hours
        # keep doubling k until we exceed target k (hours === h)
        prev, curr = 0, min(piles)
        hours = h+1
        while hours_to_eat(piles, curr) > h:
            prev = curr
            curr *= 2
        
        l, r = prev, curr
        while l < r:
            k = (l + r) // 2
            if k == 0:
                return 1
            hours = hours_to_eat(piles, k)
            if hours > h:
                l = k + 1
            else:
                r = k
        
        return l
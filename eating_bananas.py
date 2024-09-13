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
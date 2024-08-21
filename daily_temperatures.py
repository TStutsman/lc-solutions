# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         # array of temps
#         # for each temp if curr is greater remove and calc output
#         res = [0] * len(temperatures)

#         past_temp_indeces = {}
#         for idx, curr_temp in enumerate(temperatures):
#             for past_temp in past_temp_indeces.copy():
#                 if curr_temp > past_temp:
#                     past_idx = past_temp_indeces[past_temp]
#                     res[past_idx] = idx - past_idx
#                     del past_temp_indeces[past_temp]
            
#             past_temp_indeces[curr_temp] = idx
        
#         return res

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # array of temps
        # for each temp if curr is greater remove and calc output

        # O(n) set up res
        # O(n) iterate over all temps/indeces
        # - O(n^2) iterate over all past indeces
        # - worst case occurs when all past indeces are stored (constantly decreasing)

        res = [0] * len(temperatures)

        past_temp_indeces = {}
        for idx, curr_temp in enumerate(temperatures):
            for past_temp in past_temp_indeces.copy():
                if curr_temp > past_temp:
                    past_indeces = past_temp_indeces[past_temp]
                    for past_idx in past_indeces:
                        res[past_idx] = idx - past_idx
                    del past_temp_indeces[past_temp]
            
            curr_temp_indeces = past_temp_indeces.get(curr_temp, [])
            curr_temp_indeces.append(idx)
            past_temp_indeces[curr_temp] = curr_temp_indeces
        
        return res
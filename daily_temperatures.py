class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # array of temps
        # for each temp if curr is greater remove and calc output
        res = [0] * len(temperatures)

        past_temp_indeces = {}
        for idx, curr_temp in enumerate(temperatures):
            for past_temp in past_temp_indeces.copy():
                if curr_temp > past_temp:
                    past_idx = past_temp_indeces[past_temp]
                    res[past_idx] = idx - past_idx
                    del past_temp_indeces[past_temp]
            
            past_temp_indeces[curr_temp] = idx
        
        return res
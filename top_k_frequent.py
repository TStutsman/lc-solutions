class Solution:
    def topKFrequent(self, nums, k: int):
        # hash for element_counts
        # hash for most_frequent
        # for each element
            # increment it's count
            # check if it's count is greater than least most_frequent
                # if it is replace most_frequent
        # return keys from most frequent

        element_counts = {}
        most_frequent = {}
        for num in nums:
            if num in element_counts: 
                element_counts[num] += 1
            else:
                element_counts[num] = 1

            if len(most_frequent) < k:
                most_frequent[num] = element_counts[num]
            elif num in most_frequent:
                most_frequent[num] = element_counts[num]
            else:
                count, least_most = min((count, num) for num, count in most_frequent.items())
                if element_counts[num] > count:
                    del most_frequent[least_most]
                    most_frequent[num] = element_counts[num]
        
        return list(most_frequent.keys())
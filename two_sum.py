class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [1, 3, 5, 8, 9, 18], target = 26 => [3, 4]
        # each number add all other numbers and check if target O(n^2)

        # each number subtracted from the target in a new array
        # search the original for the matching value

        # target/2 = pivot = 13
        # check for double pivot
        # [1, 3, 5, 8, 9]O(n) - [18] n/2

        # array -> Dict O(n) key:value, value: index in the array
        # check every value if its partner is a key in the dict O(n)
        # return the indeces of the pair

        #[1, 3, 5, 8, 9, 18]

        # O(n) checks for if target / 2 is in solution
        if not target % 2: # true if even
            pivot = target / 2
            pivot_list = [ idx for idx, num in enumerate(nums) if num == pivot ]
            if len(pivot_list) > 1:
                return pivot_list

        # O(n) checks everything else
        num_indeces = {str(num): idx for idx, num in enumerate(nums)} #{'1':0, '3':1, '5':2...}
        for num in nums: # 8
            if str(target - num) in num_indeces and target/2 != num: # 18 true
                num1_idx = num_indeces[str(num)] # 3
                num2_idx = num_indeces[str(target - num)] # 5
                return [num1_idx, num2_idx] # [3, 5]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force O(n^2)
        # iterate over all integers i:
            # iterate over all integers after i (j):
                # if numi + numj == target, return i and j

        # 2 O(nlogn)
        # sort integers
        # iterate over all indeces i:
            # set current target = target - i
            # -- binary search for complement --
            # set pointers left = i, right = len(nums)
            # choose median number n at index (right - left//2)
            # if target - n is less than n set right equal to median

        # 3 O(n) time complexity && O(n) space complexity
        # add every num into a hash { num: idx } O(n)
        # set first_half_index equal to -1
        # for every index i O(n)
            # check if nums[i] is exactly 1/2 of target (duplicate needed)
                # if first_half_index > -1 return first_half_index, i
                # else set first_half_index equal to i
            # if not check if the complement of nums[i] exists in the hash
                # if so return i, hash[complement]

        index_of = {}
        first_half_index = -1
        for i, num in enumerate(nums):
            index_of[num] = i
        
        for i, num in enumerate(nums):
            if num * 2 == target:
                if first_half_index > -1:
                    return [first_half_index, i]
                else:
                    first_half_index = i
            else:
                complement = target - num
                if complement in index_of:
                    return [i, index_of[complement]]
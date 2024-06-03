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
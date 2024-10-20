# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # naive approach: uses O(n) space for the set
#         visited = set();

#         for num in nums:
#             if num in visited:
#                 return num
#             visited.add(num)

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Initialize slow and fast locations
        slow, fast = nums[0], nums[nums[0]]

        # Find the loop in the linked list
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow = nums[slow]
            slow2 = nums[slow2]

        return nums[slow]
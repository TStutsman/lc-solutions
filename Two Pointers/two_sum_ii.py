class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
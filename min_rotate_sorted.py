class Solution:
    def findMin(self, nums: List[int]) -> int:
        # cut the circle in half - circle again
        # how to determine which half to remove?
        # the half with the min number will have
        # split array in half
        # mult a[0] * a[-1] vs b[0] * b[-1]
        # smaller value contains min
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            a = nums[l] * nums[m]
            b = nums[m + 1] * nums[r]

            print(m, a, b)

            if a < b:
                r = m
            elif b < a:
                l = m + 1
            else:
                print("ERROR")
                return
        
        return nums[l]

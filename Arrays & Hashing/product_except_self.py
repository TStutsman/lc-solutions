class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # brute force
        # for every element at i
        # iterate over all other elements multiplying
        # ------- 0(n^2) time O(1) space --------

        # division
        # multiply every number together
        # for every element i
        # divide product by nums[i]
        # ------- O(n) time O(1) space ---------

        # non-division
        # stack of products
        # for every element except the last
        # peek at the top of the stack and multiply
        # push product onto stack
        
        # save product n = 1
        # for every element at index i from last -> first
        # pop off stack = product(i)
        # multiply n by element at i
        # pop off stack and multiply by n = product(i-1)
        # push back onto stack

        stack = [nums[-1]]
        for i in range(len(nums)-2, 0, -1):
            product = stack[-1] * nums[i]
            stack.append(product)

        products_arr = []
        accumulator = 1
        for i in range(len(nums) - 2):
            products_arr.append(stack.pop())

            accumulator *= nums[i]
            stack[-1] *= accumulator

        products_arr.append(stack.pop())
        products_arr.append(accumulator * nums[-2])

        return products_arr
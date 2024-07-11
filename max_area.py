class Solution(object):
    def calcArea(self, l, r, height):
        return (r-l) * min(height[l], height[r])

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # HELPER FUNCTION (area)
        # Need to calculate the amount of water (area)
        # Lowest value length (h) * distance between lines (w) = area (amt water)

        # Left and Right pointers either side of height array
        # check area, save to max
        # move the pointer with the lower height line
        # repeat until left >= right
        l, r = 0, len(height) - 1
        curr_max = self.calcArea(l, r, height)

        while l < r:
            curr_l = l
            while height[l] < height[r]:
                l += 1
                if height[curr_l] < height[l]:
                    curr_area = self.calcArea(l, r, height)
                    curr_max = max(curr_max, curr_area)

            curr_r = r
            while height[r] <= height[l] and l < r:
                r -= 1
                if height[curr_r] < height[r]:
                    curr_area = self.calcArea(l, r, height)
                    curr_max = max(curr_max, curr_area)


        return curr_max
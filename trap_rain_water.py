class Solution:
    def trap(self, height: list[int]) -> int:
        # when next decreases, start adding to area
        # curr_area += height[l] - pillar
        # when increasing, set next_max
        # if next_max >= height[l]
        # - max_area += curr_area
        # last condition is if r reaches the end of the array

        l = 0
        max_area, curr_area, prev, next_max = 0,0,0,0

        # O(n)
        for r, pillar in enumerate(height):

            if pillar >= height[l]:
                max_area += curr_area
                curr_area = 0
                l = r
            else:
                curr_area += height[l] - pillar

            if pillar > prev:
                next_max = r
        
            prev = pillar

        # O(n)
        # last condition is if r reaches the end of the array
        # need to account for depth of next_max if lower than height[l]
        if l < next_max:
            for idx in range(l, next_max+1):
                if height[idx] < height[next_max]:
                    max_area += height[next_max] - height[idx]
        
        return max_area
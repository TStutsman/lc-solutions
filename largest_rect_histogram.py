class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # area = (r - l) * min_height

        # max = heights at zero

        # for each l
            # for each r
                # check heights[r] for new min

                # if (r - l) * min > max
                    # max = (r - l) * min
                # if len(heights) - r * min <= max
                    # break

        max_rec = 0

        for l in range(len(heights)):
            curr_min = heights[l]
            for r in range(l, len(heights)):
                curr_min = min(curr_min, heights[r])

                curr_rec = (r - l + 1) * curr_min
                max_rec = max(max_rec, curr_rec)

                if (len(heights) - l) * curr_min <= max_rec:
                    break

        return max_rec
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # split on median of each array
        # compare medians to find larger/smaller
        # if medians are the same return
        # else remove larger than larger median in it's array
        # and remove smaller than smaller median it it's array
        # if one array is empty, return median of nonempty array

        def median(arr, left, right) -> tuple[int, int]:
            mid = (right + left) // 2
            if (right + left) % 2:
                # calculate median, idx is ceiling
                return (arr[mid] + arr[mid + 1]) / 2, mid + 1
            return arr[mid], mid

        l1, r1 = 0, len(nums1) - 1
        l2, r2 = 0, len(nums2) - 1

        # exit when one has no nums left
        while r1 >= l1 and r2 >= l2:
            median1, mid1 = median(nums1, l1, r1)
            median2, mid2 = median(nums2, l2, r2)

            # if they both have only one num left, calculate median
            if l1 == r1 and l2 == r2:
                return (median1 + median2) / 2

            if median1 > median2:
                r1 = mid1 - 1
                l2 = mid2
            elif median2 > median1:
                l1 = mid1
                r2 = mid2 - 1
            else:
                return median1

        if l1 > r1:
            return median(nums2, l2, r2)[0]

        return median(nums1, l1, r1)[0]
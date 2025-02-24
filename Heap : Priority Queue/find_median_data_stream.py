import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        median = self.findMedian()

        if median and num < median:
            if len(self.lower) > len(self.higher):
                old_median = -heapq.heappushpop(self.lower, -num)
                heapq.heappush(self.higher, old_median)
            else:
                heapq.heappush(self.lower, -num)

        else:
            if len(self.higher) > len(self.lower):
                old_median = heapq.heappushpop(self.higher, num)
                heapq.heappush(self.lower, -old_median)
            else:
                heapq.heappush(self.higher, num)

    def findMedian(self) -> float:
        if len(self.lower) == len(self.higher):
            if not self.higher:
                return None
                
            return (self.higher[0] - self.lower[0]) / 2

        median = -self.lower[0] if len(self.lower) > len(self.higher) else self.higher[0]
        return float(median)
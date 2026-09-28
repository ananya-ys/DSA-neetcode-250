import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (smaller half)
        self.large = []  # Min heap (larger half)

    def addNum(self, num: int) -> None:
        # Add number to max heap (using negative values)
        heapq.heappush(self.small, -num)

        # Move the largest element of small to large
        heapq.heappush(
            self.large,
            -heapq.heappop(self.small)
        )

        # Balance the heaps
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(
                self.small,
                -heapq.heappop(self.large)
            )

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.large) > len(self.small):
            return float(self.large[0])

        # Even number of elements
        return (self.large[0] - self.small[0]) / 2.0
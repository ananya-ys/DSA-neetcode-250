from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n):

        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        time = 0

        while heap:

            temp = []

            # One CPU cycle
            for _ in range(n + 1):

                if heap:
                    freq = heapq.heappop(heap)
                    freq += 1

                    if freq != 0:
                        temp.append(freq)

                time += 1

                if not heap and not temp:
                    break

            # Put unfinished tasks back
            for freq in temp:
                heapq.heappush(heap, freq)

        return time
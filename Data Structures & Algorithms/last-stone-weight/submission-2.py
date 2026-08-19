import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
            if largest != second_largest:
                diff = largest - second_largest
                heapq.heappush(max_heap,-diff)

        if not max_heap:
            return 0

        return -max_heap[0]

        
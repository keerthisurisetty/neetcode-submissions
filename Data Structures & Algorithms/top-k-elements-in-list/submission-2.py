class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for x, y in freq.items():
            heapq.heappush(heap, (y,x))
            if len(heap) > k:
                heapq.heappop(heap)
        return[x for y, x in heap]

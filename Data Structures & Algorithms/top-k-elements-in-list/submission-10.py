class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        res = []
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        for n in freq.keys():
            heapq.heappush(min_heap, (freq[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for f, n in min_heap:
            res.append(n)

        return res
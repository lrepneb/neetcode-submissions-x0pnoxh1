class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # pop top 2
            big1, big2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            result = abs(big1-big2)
            if result != 0:
                heapq.heappush_max(stones, result)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
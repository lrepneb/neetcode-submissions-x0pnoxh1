class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weight):
            d, capacity = 1, weight

            for w in weights:
                if capacity < w:
                    d+=1
                    capacity = weight
                capacity-=w
            return d <= days

        max_weight = max(weights)
        sum_weights = sum(weights)

        l, r = max_weight, sum_weights
        min_weight = sum_weights
        while l<=r:
            mid = (l + r) // 2

            if canShip(mid):
                min_weight = min(min_weight, mid)
                r = mid - 1
            else:
                l = mid + 1
        return min_weight

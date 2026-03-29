class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        zs = [0] * len(set(nums))
        d = {ke:v for ke, v in zip(set(nums), zs)}
        for n in nums:
            d[n] += 1
        tup_list = list(d.items())
        # return tup_list
        sorted_l = sorted(tup_list, reverse = True, key = lambda x:x[1])
        return [ke for ke, v in sorted_l[:k]]
        # return sorted_l[:k]


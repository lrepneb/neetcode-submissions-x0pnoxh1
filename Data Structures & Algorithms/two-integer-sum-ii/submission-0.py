class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1, i2 = 0, len(numbers)-1
        res = numbers[i1] + numbers[i2]
        while res != target and i1 < i2:
            if res < target:
                i1+=1
            elif res > target:
                i2-=1
            res = numbers[i1] + numbers[i2]
        return [i1+1, i2+1]

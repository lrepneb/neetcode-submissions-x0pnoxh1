class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red -> white -> blue
        # insertion sort with 3 buckets
        # keep track of where white begins
        white_start = 0

        for i in range(len(nums)):
            color = nums.pop(i)
            ind = 0
            # red -> send to front
            if color == 0:
                ind = 0
                white_start+=1
            # white -> end to white_start
            elif color == 1:
                ind = white_start
                white_start+=1
            # blue -> send to back (current index)
            else:
                ind = i
            nums.insert(ind, color)

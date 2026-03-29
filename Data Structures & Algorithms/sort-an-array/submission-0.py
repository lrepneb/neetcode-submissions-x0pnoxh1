class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge
        def merge(arr, left, mid, right):
            l_arr, r_arr = arr[left:mid+1], arr[mid+1:right+1]
            ap, lp, rp = left, 0, 0
            while lp < len(l_arr) and rp < len(r_arr):
                if l_arr[lp] > r_arr[rp]:
                    arr[ap] = r_arr[rp]
                    rp+=1
                else:
                    arr[ap] = l_arr[lp]
                    lp+=1
                ap+=1

            #check whether its lp or rp that went over
            while lp < len(l_arr):
                arr[ap] = l_arr[lp]
                ap+=1
                lp+=1
            while rp < len(r_arr):
                arr[ap] = r_arr[rp]
                ap+=1
                rp+=1

        def mergeSort(arr, left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)
            merge(arr, left, mid, right)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums

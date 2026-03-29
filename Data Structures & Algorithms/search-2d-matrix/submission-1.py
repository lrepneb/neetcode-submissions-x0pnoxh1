class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_rows, r_rows = 0, len(matrix) - 1
        l_cols, r_cols = 0, len(matrix[0]) - 1
        # find row via binary search
        ## 1. Take middle row: is the target above
        ## matrix[middle][len(matrix[0]), below
        ## matrix[middle][0] or somewhere in between?
        while l_rows <= r_rows:
            # take middle row
            m = (l_rows + r_rows) // 2
            if matrix[m][0] > target:
                r_rows = m-1
            elif matrix[m][r_cols] < target:
                l_rows = m+1
            else:
                while l_cols <= r_cols:
                    m2 = (l_cols + r_cols) // 2
                    if matrix[m][m2] > target:
                        r_cols = m2-1
                    elif matrix[m][m2] < target:
                        l_cols = m2+1
                    else:
                        return True
        return False
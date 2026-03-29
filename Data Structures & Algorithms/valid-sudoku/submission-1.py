class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={k:[] for k in range(9)}
        col={k:[] for k in range(9)}
        box={k:[] for k in range(9)}
        for r, v in enumerate(board):
            for c, val in enumerate(v):
                # CHECK
                if val == ".":
                    continue
                # row
                if val in row[r]:
                    return False
                row[r].append(val)
                # col
                if val in col[c]:
                    return False
                col[c].append(val)
                # 3x3 box
                b = int(r//3) + int((c//3) * 3)
                if val in box[b]:
                    return False
                box[b].append(val)
        return True
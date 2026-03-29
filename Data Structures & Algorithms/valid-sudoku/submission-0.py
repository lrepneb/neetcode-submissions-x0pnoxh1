class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={k:[] for k in range(9)}
        col={k:[] for k in range(9)}
        box={k:[] for k in range(9)}
        for r, v in enumerate(board):
            print(v)
            for c, val in enumerate(v):
                # CHECK
                if val == ".":
                    continue
                print("starting row")
                # row
                if val in row[r]:
                    # row[r].append(val)
                    print(r, c, val, row, col, box)
                    return False
                row[r].append(val)
                # col
                print("starting col")
                if val in col[c]:
                    # col[c].append(val)
                    print(r, c, val, row, col, box)
                    return False
                col[c].append(val)
                # 3x3 box
                print("starting box")
                rc = r//3
                cc = (c//3) * 3
                b = int(rc) + int(cc)
                if val in box[b]:
                    # box[b].append(val)
                    print(r, c, b, val, row, col, box)
                    return False
                box[b].append(val)
        print(row, col, box)
        return True
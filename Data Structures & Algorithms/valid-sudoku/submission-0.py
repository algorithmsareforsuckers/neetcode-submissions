class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counts = {}
        col_counts = {}
        sub_boxes = {}

        for j in range(len(board)):
            # j fixes row
            for i in range(len(board[j])):
                # i fixes column
                val = board[j][i]
                if val == ".":
                    continue

                # zero index
                val = int(val) - 1

                row_counts[j] = row_counts.get(j, [0]*9)
                row_counts[j][val] += 1
                if row_counts[j][val] > 1:
                    return False

                col_counts[i] = col_counts.get(i, [0]*9)
                col_counts[i][val] += 1
                if col_counts[i][val] > 1:
                    return False

                # subbox (x,y) can be determined by (i//3, y//3)
                # to index dict just to i//3*10 + y//3
                sb_index = (i//3)*10 + j//3
                sub_boxes[sb_index] = sub_boxes.get(sb_index, [0]*9)
                sub_boxes[sb_index][val] += 1
                if sub_boxes[sb_index][val] > 1:
                    return False


        return True

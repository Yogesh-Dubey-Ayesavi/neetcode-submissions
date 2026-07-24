class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxes = [set() for _ in range(9)]
        for i in range(9):
            row_set = set()
            column_set = set()
            for j in range(9):
                # Row check

    
                value = board[i][j]
                if value != '.':
                    if value in row_set:
                        return False
                    row_set.add(value)
                
                box = (i // 3) * 3 + (j // 3)
                
                # box check
                if value != '.':
                    if value in boxes[box]:
                        return False
                    
                    boxes[box].add(value)

                # Column check
                value = board[j][i]

                if value != '.':
                    if value in column_set:
                        return False
                    column_set.add(value)


        return True
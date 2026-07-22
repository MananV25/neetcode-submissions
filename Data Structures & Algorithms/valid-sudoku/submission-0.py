class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for rows in board:
            row = set()
            for cell in rows:
                if cell == ".":
                    continue
                if cell in row:
                    return False
                row.add(cell)

        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]

                if cell ==".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for r in range(3):
                    for c in range(3):

                        cell = board[i+r][j+c]
                        if cell ==".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        return True

                        

             


        

        
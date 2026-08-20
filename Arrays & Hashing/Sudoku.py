"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c]) == ".":
                    continue
                if( board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
"""                 
"""
The plan of this was to use 3 hashmaps to keep track of the numbers we have seen in each row, column, and 3x3 square. We iterate through the board and for each number, we check if it has already been seen in the corresponding row, column, or square. If it has, we return False. If we finish iterating through the board without finding any duplicates, we return True.
"""
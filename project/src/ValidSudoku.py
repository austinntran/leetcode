from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            uniqueSet =set()
            row = board[y]
            for x in range(9):
                value = row[x]
                if value != ".":
                    initialLength = len(uniqueSet)
                    uniqueSet.add(value)
                    if len(uniqueSet) == initialLength:
                        return False
            col = self.column(board, y)
            uniqueSet =set()
            for x in range(9):
                value = col[x]
                if value != ".":
                    initialLength = len(uniqueSet)
                    uniqueSet.add(value)
                    if len(uniqueSet) == initialLength:
                        return False
        for r in range(3):
            for c in range(3):
                if self.threeByThreeContainsDuplicates(board, r, c):
                    return False
        return True
    def column(self, matrix, i):
        return [row[i] for row in matrix]
    def threeByThreeContainsDuplicates(self, board, x, y):
        rowNumber = x * 3
        columnNumber = y * 3
        uniqueSet =set()
        for r in range(rowNumber, rowNumber + 3):
            for c in range(columnNumber, columnNumber + 3):
                value = board[r][c]
                if value != ".":
                    initialLength = len(uniqueSet)
                    uniqueSet.add(board[r][c])
                    if len(uniqueSet) == initialLength:
                        return True
        return False
                
                
    
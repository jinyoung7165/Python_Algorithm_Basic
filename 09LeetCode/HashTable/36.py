#Valid Sudoku. 9*9크기
#각 행,열은 1-9 중복없이 가짐
#3*3부분 맵은 1-9 중복없이 가짐
#값이 존재하는 부분만 판단하면 됨
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(arr):
            s = ''.join(arr).replace('.','') #.제거, 모두 이어붙임
            return len(s) == len(set(s)) #중복 없어야 함
        
        # Check each row in the board
        def checkRow():
            for row in board:
                if not isValid(row):
                    return False
            return True
        
        # Check each col in the board,
        # To access each col, we first unpack the board into sperate lists using *
        # We then zip these rows together into columns.
        def checkCol():
            for col in zip(*board):
                if not isValid(col):
                    return False
            return True
        
        # To get each sub-box, we first get the top-left indices of each sub-box,
        # We then go 3 steps on each row and 3 steps on each col to construct the box.
        def checkSub():
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    sub = [board[i+k][j+t] for k in range(3) for t in range(3)]
                    if not isValid(sub):
                        return False
            return True
        
        # In order to be a valid Sudoku, all row, col, and sub-box need to be valid
        return checkRow() and checkCol() and checkSub()
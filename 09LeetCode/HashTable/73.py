#73. Set Matrix Zeroes
#원소가 0이면 해당 행, 열 모두 0으로 세팅해라
#in-place로 해결하라. 공간 O(1)로 쓰기 위해 해당 행의 0열, 해당 열의 0행에 표시 후 0행, 0열을 보고 0으로 치환
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1 and n == 1:
            return matrix
        
        flag_row = False
        flag_col = False
        
        for i in range(m):
            if matrix[i][0] == 0: #0열에 0이 있으면-0열의 모든 행 0으로 만들 것
                flag_col = True
                break
                
        for i in range(n):
            if matrix[0][i] == 0: #0행에 0이 있으면-0행의 모든 열 0으로 만들 것
                flag_row = True
                break
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 #해당 열의 0행 원소를 0으로
                    matrix[i][0] = 0 #해당 행의 0열 원소를 0으로
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        
        if flag_row:
            for j in range(n):
                matrix[0][j] = 0
        if flag_col:
            for i in range(m):
                matrix[i][0] = 0
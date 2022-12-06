#73. Set Matrix Zeroes
#원소가 0이면 해당 행, 열 모두 0으로 세팅해라
#in-place로 해결하라
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rLen,cLen=len(matrix),len(matrix[0])
    
        #row=[1]*rLen
        
        col=[1]*cLen 
        
        for r in range(rLen):
            flag=0 
            for c in range(cLen):
                
                if matrix[r][c]==0:
                    flag=1
                    col[c]=0
            
            if flag:
                matrix[r]=[0]*cLen
                   
        for r in range(rLen):
            for c in range(cLen):
                if col[c]==0:
                    matrix[r][c]=0
            
            
        return matrix
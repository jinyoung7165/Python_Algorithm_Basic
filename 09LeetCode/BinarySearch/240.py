#2D행렬에서 값 존재하면 true/false
#행 안에서는 정렬돼 있음
#열 안에서는 정렬돼 있음

#첫 행의 마지막 원소 택한 다음, 타겟보다 크면 왼쪽으로, 작으면 아래로 이동
def searchMatrix(self, matrix, target):
    if not matrix:
        return False
    
    #첫 행의 맨뒤
    row = 0
    col = len(matrix[0]) - 1
    
    while row <= len(matrix)-1 and col >= 0:
        if target == matrix[row][col]:
            return True
        ##타겟이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
    return False
#파이썬다운 방식
def searchMatrix(self, matrix, target):
    return any(target in row for row in matrix) #위에서 차례대로 탐색
#프렌즈 4블록
def solution(n, m, board):
    board = [list(x) for x in board]
    
    matched = True
    #일치 여부 판별
    while matched:
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == \
                    board[i][j+1] == \
                    board[i+1][j+1] == \
                    board[i+1][j] != '#':
                        matched.append([i,j])
    #일치한 위치 삭제
    for i, j in matched:
        board[i][j] = board[i][j+1] = board[i+1][j+1] = board[i+1][j] = '#'
        
    
    #빈 공간 블럭 삭제
    for _ in range(m):
        for i in range(m-1):
            for j in range(n-1):
                if board[i+1][j] == '#':
                    board[i+1][j], board[i][j] = board[i][j], '#'
    return sum(x.count('#') for x in board)
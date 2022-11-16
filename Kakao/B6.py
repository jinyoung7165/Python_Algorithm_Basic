#프렌즈 4블록
#2x2형태의 블록이 4개 존재
#조건에 만족하는 블록들 4칸묶음으로 (겹치기 가능)지워짐 -> 빈 공간을 위의 블록들이 떨어지며 채움
#지워지는 블록의 개수 구하라
def solution(m, n, board):
    board = [list(x) for x in board]
    
    matched = True
    while matched:
    #일치 여부 판별
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '#' and board[i][j] == board[i][j+1] \
                    == board[i+1][j] == board[i+1][j+1]:
                        matched.append([i, j]) #4칸 시작위치 기억
        #일치한 위치 삭제
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j+1] = board[i+1][j] = '#'
            
        
        #빈 공간 블럭 삭제
        for _ in range(m-1): #아래와 swap 후, 그 위의 블록도 현재와 swap 가능한지 봐야함
            for i in range(m-1): #아래와 swap
                for j in range(n-1):
                    if board[i+1][j] == '#': #아랫칸과 비교 -> swap
                        board[i+1][j], board[i][j] = board[i][j], '#'
        print(board)
    return sum(x.count('#') for x in board) #빈 공간 개수 세기


print(solution(4,5,["CCBDE","AAADE","AAABF","CCBBF"])) #14
#A6개 ->B4, C4개 지워짐
print(solution(6,6,["TTTANT","RRFACC","RRRFCC","TRRRAA","TTMMMF","TMMTTJ"])) #15
#11, 4 지워짐
#같은 문자가 2X2 이상이 되면 지워짐, 빈 공간을 위에서 채움
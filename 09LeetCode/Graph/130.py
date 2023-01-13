#Surrounded Regions
#사방이 N으로 막혀있는 O영역을 N으로 바꿔라
#border이 O이거나 그것과 연결된 곳은 바꿀 수 없음
#BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #border에 존재하거나, 그것과 붙어있는 O라면 바뀌면 안됨
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R<=2 or C<=2: #border만 존재
            return
        queue = collections.deque()
        for i in range(R):
            for j in range(C):
                if i in [0, R-1] or j in [0, C-1] and board[i][j] == 'O': #border에 있는 O이면 넣어줌
                    queue.append([i, j])
        while queue:
            x, y = queue.popleft()
            if 0<=x<R and 0<=y<C and board[x][y] == 'O':
                board[x][y] = '.' #border O거나 그것과 붙어있는 부분
                queue.append([x, y-1])
                queue.append([x, y+1])
                queue.append([x+1, y])
                queue.append([x-1, y])

        for i in range(R):
            for j in range(C):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
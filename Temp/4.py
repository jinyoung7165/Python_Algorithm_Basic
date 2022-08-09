#격자정보 grid, 하루 최대 이동 횟수 k
#(1,1)에서 (n,m)로 이동하기 위한 최소 야영횟수를 return
#.평지(야영가능), F숲, #못감
d = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(x,y,grid):
    n, m = len(grid), len(grid[0])
    grid[x][y] = -1 #방문처리
    for i in range(4): #다음 방향
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<n and 0<=dy<m and grid[dx][dy] == 1:
            dfs(dx,dy)
    
def solution(grid, k):
    count = len(grid[0])
    n, m = len(grid), len(grid[0])
    
    dfs(0,0,grid) #출발
    
    return count

print(solution(["..FF","###F","###."], 4)) #1
print(solution(["..FF","###F","###."], 5)) #0
print(solution([".F.FFFFF.F",".########.",".########F","...######F","##.######F","...######F",".########.",".#...####F","...#......"], 6)) #3
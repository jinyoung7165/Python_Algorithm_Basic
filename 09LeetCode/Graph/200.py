#0,1 맵 주어짐 -> 연결된 1의 덩어리 개수 구하라

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0으로 둘러싸인 지역의 개수
        m, n = len(grid), len(grid[0])
        count = 0
        def dfs(x, y):
            print(x,y)
            if 0<=x<m and 0<=y<n and grid[x][y] == '1':
                grid[x][y] = -1 # 방문 처리
                # 육지 -> 계속 이동 가능
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 육지면 계속 갈 수 있음
                    dfs(i, j)
                    count += 1
        return count
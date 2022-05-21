#0,1 맵 주어짐 -> 연결된 1의 덩어리 개수 구하라

#graph = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
graph = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]


def dfs(x,y):
    if 0 > x  or x >= 4 or 0 > y or y >= 5 or graph[x][y]!= 1:
        return

    graph[x][y] = -1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)

def main():            
    count = 0 
    for i in range(4):
        for j in range(5):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    return count

print(main())
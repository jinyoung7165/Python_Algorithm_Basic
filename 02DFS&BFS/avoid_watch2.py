from itertools import combinations
 
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
n = int(input())
graph = [[' '] for _ in range(n + 1)]
empty = list()
teachers = list()
for i in range(1, n + 1):
    graph[i] += input().split()
    for j in range(1, n + 1):
        if graph[i][j] == 'X':
            empty.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))
 
for obj in combinations(empty, 3):
    for y, x in obj:
        graph[y][x] = 'O'
 
    flag = False #학생을 찾았는지
    for teacher in teachers:
        for i in range(4):#상하좌우 방향
            y, x = teacher #선생님의 x,y좌표
            while 1 <= y <= n and 1 <= x <= n and graph[y][x] != 'O': #이동한 곳이 O이면 다른 방향 탐색할 거다
                if graph[y][x] == 'S': #학생 찾았다
                    flag = True
                    break
                y += dd[i][0]
                x += dd[i][1]
            if flag: #이미 찾은 상태면 다른 방향 탐색할 필요 없음
                break
        if flag:#이미 찾은 상태면 다른 선생도 탐색할 필요 없음
            break
 
    if not flag:
        print('YES')
        exit()
 
    for y, x in obj:
        graph[y][x] = 'X'
 
print('NO')

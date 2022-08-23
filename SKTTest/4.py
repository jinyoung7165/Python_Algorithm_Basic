#격자정보 grid, 하루 최대 이동 횟수 k
#(1,1)에서 (n,m)로 이동하기 위한 최소 야영횟수를 return
#.평지(야영가능), F숲, #못감
'''
1. BFS 하나만 이용할 때 갔다가 돌아오면 안되니까 → visited 사용하면 하나의 경로밖에 탐색 못함
BFS→ 각 갈래마다 한 칸씩 전진하면서 가까울수록 노드 빨리 차지, but, 여기선 다른 갈래한테도 같은 노드를 내어줘야 함
DP-> 다시 방문하면 이전에 저장한 값 사용 -> visited를 set/list가 아닌 dictionary로 만들어야한다
1. 설명을 보니 **모든 갈래의 경로를 출발-도착까지 나열**해서 비교한다
2. 왜냐면, 해당 노드는 어떤 경로에 속하는지에 따라 야영 유무가 다름
3. DFS로 풀어야 한다

1. dfs지나온 애 다시 원상복구 큐
2. dp+dfs 백트래킹 - 이 노드를 선택했을 때/안 했을 때? -> 노드 마지막부터 거꾸로 보면 선택 기준 알 듯
3. 경로 미리 다 저장해서 각 경로의 result 구하기
'''
d = [[0,1],[1,0],[0,-1],[-1,0]]

from collections import deque


dp = []
    
def solution(grid, k):
    n, m = len(grid), len(grid[0]) #행열
    
    result = n*m #야영횟수
    
    for i in range(n): #string map -> int map
        temp = []
        for j in range(m):
            if grid[i][j] == '.': #평지 -> 야영 가능
                temp.append(1)
            elif grid[i][j] == 'F': #숲
                temp.append(0)
            else:
                temp.append(-1) #이동 불가
        dp.append(temp)
       
    que = deque([[0, k, 0, 0, 0, []]]) #야영 횟수, 남은 K, 연속 F수, 시작 위치
    
    while que:
        sleep, K_remain, F_count, x, y, path = que.popleft() #야영 횟수, 남은 k, 앞의 연속 F, 현재 위치, 지나온 길
        
        if x == n-1 and y == m-1: #도착 시 최소 갱신
            result = min(result, sleep)
            continue
        
        
        if K_remain == 0: #이동 불가
            if dp[x][y] == 1: #현재 평지면 여기에 바로 야영하자
                sleep += 1
                K_remain = k
            else: #현재 숲이라 이전에 야영했어야 함
                if F_count > 0: #이전 좌표가 F였으면
                    if k - F_count > 0:#야영을 했다 쳤을 때 연속F 개수가 k보다 작아야 다음 차례에 움직일 수 있음
                        sleep += 1 #야영
                        K_remain = k - F_count - 1 #갱신된 k - 연속F수
                    else:
                        continue
                else: #이전 좌표가 .이었으면
                    sleep += 1 #이전에 야영 가능
                    K_remain = k - 1
                
        if sleep > result: continue #가봤자 최소가 아님
        
        #남은 k, 연속 F 수 업데이트
        K_remain -= 1
        
        if dp[x][y] == 0: F_count += 1 #F일 때 연속으로 나온 F수 증가
        else: F_count = 0
        
        temp = path[:]
        temp.append([x, y]) #지나온 경로에 추가
        
        for i in range(4): #다음 방향
            dx = x+d[i][0]
            dy = y+d[i][1]
            if 0<=dx<n and 0<=dy<m and dp[dx][dy] != -1 and [dx, dy] not in temp: #이동 가능
                que.append([sleep, K_remain, F_count, dx, dy, temp])
                
    return result

# queue,,무한히 사방팔방으로 가면 안되는데,,,visit써버리면 하나의 경로밖에 탐색 못함
print(solution(["..FF","###F","###."], 4)) #1
#print(solution(["..FF","###F","###."], 5)) #0
#print(solution([".F.FFFFF.F",".########.",".########F","...######F","##.######F","...######F",".########F",".########.",".#...####F","...#......"], 6)) #3
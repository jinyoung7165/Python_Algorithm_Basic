#백준 3190 - 뱀
#사과를 먹으며 몸길이가 늘어남
#다음 칸에 사과가 있으면 이전칸의 꼬리 그대로 위치
#사과가 없으면 몸 길이 변하지않음
#벽에 닿거나 몸에 부딪치면 끝
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]
graph[0][0] = 2 #뱀의 위치

k = int(input()) #사과 개수
for _ in range(k): #사과 위치
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1
    
l = int(input()) #방향 변환 수
times = {} #해당 시간 후 위치를 바꿀 것
for i in range(l): #x초가 끝난 뒤 L(왼) 또는 D(오) 90도 회전
    x, c = input().split()
    times[int(x)] = c

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상->우->하->좌->상: +1 방향
    # 왼쪽 회전: 상->좌->하->우->상: -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def start():
    time, direction = 1, 1 #초기 시간, 방향
    x, y = 0, 0 #현재 위치
    que = deque([[0, 0]]) #뱀의 위치
    while True:
        y, x = y + dy[direction], x + dx[direction] #현재 위치
        if 0 <= y < n and 0 <= x < n and graph[y][x] != 2: #벽, 자기자신이 아닐 때
            if not graph[y][x] == 1: #사과x
                last_y, last_x = que.popleft()
                graph[last_y][last_x] = 0 #꼬리 제거
            graph[y][x] = 2 #현재 위치에 뱀 둔다
            que.append([y, x])
            if time in times.keys(): #현재 시간에 방향 바꾸는지 확인
                direction = change(direction, times[time])
            time += 1
                
        else: return time
        
print(start())
#방문한 칸의 수 출력
n,m=map(int,input().split())
x,y,direction=map(int,input().split()) #(a,b) 바라보는 방향 direction
#- 0: 북쪽- 1: 동쪽- 2: 남쪽- 3: 서쪽
visited=[[0]*m for _ in range(n)]
visited[a][b]=1 #현재 좌표 방문 처리

mapp=[]#0은 육지, 1은 바다
for _ in range(n):
    mapp.append(list(map(int,input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction-=1 #왼쪽으로 회전
    if direction ==-1: #북에서 왼쪽
        direction=3

count=1 #이동한 칸의 수
turn_time=0 #네 방향 모두 확인했는지
while True:
    turn_left()#왼쪽으로 회전
    nx=x+dx[direction]#왼쪽으로 이동
    ny=y+dy[direction]
    #회전한 이후에 가보지 않은 육지 칸이 존재하는 경우 이동
    if visited[nx][ny]==0 and mapp[nx][ny]==0:
        x=nx
        y=ny #정해진 곳으로 이동
        count+=1
        turn_time=0
        continue
    else: #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        turn_time+=1 #고개만 돌릴 것이다
    if turn_time==4:#네 방향 모두 갈 수 없는 경우
        nx=x-dx[direction]
        ny=y-dy[direction] #후진
        if mapp[nx][ny]==0: #육지인 경우
            x=nx
            y=ny
        else:
            break
        turn_time=0
print(count)


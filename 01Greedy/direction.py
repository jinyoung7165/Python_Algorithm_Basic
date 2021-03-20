'''
N x N 크기의 정사각형 공간. 가장 왼쪽 위 좌표는 (1,1),가장 오른쪽 아해 좌표는 (N,N)
상,하,좌,우 로 이동할 수 있으며, 시작좌표는 (1,1). 
L: 왼쪽으로 한 칸
R: 오른쪽으로 한 칸
U: 위로
D: 아래로
공간 밖으로 넘어가는 지시는 무시한다.
'''
n=int(input()) #공간 전체 크기 n x n
x,y=1,1 #현재 위치
plans=input().split() #이동 지시

# 동,서,남,북
dx=[0,0,-1,1]
dy=[-1,1,0,1]
move_types=['L','R','U','D']

for plan in plans: #이동 지시 확인
    for i in range(len(move_types)): #좌표 이동
        if plan==move_types[i]:
            nx=x+dx[i] #다음 위치
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: #공간에서 벗어나면
        continue
    x,y=nx,ny #다음 위치로 이동

print(x,y)
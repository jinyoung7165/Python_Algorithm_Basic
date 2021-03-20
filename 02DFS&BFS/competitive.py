from collections import deque
n,k=map(int,input().split()) #col수, 바이러스 종류
maps=[]
data=[]#바이러스에 대한 정보(종류,시간,x,y좌표)
for i in range(n):
    maps.append(list(map(int,(input().split()))))
    for j in range(n):#해당 위치에 바이러스가 존재하는 경우
        if(maps[i][j]!=0):
            data.append((maps[i][j],0,i,j)) #초기 바이러스 정보 입력
data.sort() #낮은 번호의 바이러스부터 증식하므로 정렬!!
que=deque(data) #정렬 덕분에 숫자가 작은 바이러스가 자리를 선점할 수 있다.

s,ex,ey=map(int,input().split()) #s초뒤,(ex,ey)에 존재하는 바이러스 종류를 출력해야함

dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]

while que: #큐가 빌 때까지 반복(bfs)
    virus,time,x,y=que.popleft() #현재 상태
    if time==s:
        break
    for i in range(4): #상하좌우 위치 확인
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<=n-1 and 0<=ny<=n-1: #해당 위치로 이동할 수 있는 경우
            if maps[nx][ny]==0: #비어 있는 경우 이동
                maps[nx][ny]=virus
                que.append((virus,time+1,nx,ny))
print(maps[ex-1][ey-1]) #[1,1] 부터 시작하는 것으로 간주하므로 한 칸씩 당겨와야 한다
            
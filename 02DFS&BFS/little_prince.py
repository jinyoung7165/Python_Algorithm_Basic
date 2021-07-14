#백준 1004 - 어린 왕자
#최소의 행성계 진입/이탈 횟수를 구하라
for _ in range(int(input())): #각 테스트케이스
    maps=[] #중신좌표, 반지름
    x1,y1,x2,y2=map(int,input().split())#출발좌표, 도착좌표
    n=int(input())#행성계 개수
    include=[0]*n
    for i in range(n):#행성 중점,반지름
        maps.append(list(map(int,input().split())))
        if((maps[i][0]-x1)**2+(maps[i][1]-y1)**2<=maps[i][2]**2):
            include[i]+=1
        if((maps[i][0]-x2)**2+(maps[i][1]-y2)**2<=maps[i][2]**2):
            include[i]+=1
    sum=0
    for i in range(n):
        if include[i]!=2: #둘 다 속한 경우가 아닐때
            sum+=include[i]    
    print(sum)

#백준 2457 - 공주님의 정원
#3월 1일~11월 30일까지 매일 꽃이 한 개 이상 피어있어야 함
#선택한 꽃의 최소 수를 출력
#4,6,9,11월은 30일까지, 1,3,5,7,8,10,12월은 31일까지, 2월은 28일까지 존재
from sys import stdin
import heapq 
from collections import deque
input=stdin.readline

date={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
min=[3,1]
max=[11,30]  #시작 기한,마감 기한

n=int(input()) #전체 꽃 개수
flower=[-1]*n #각 꽃의 피는 날,지는 날 저장
select=[]
q=[] #모든 flower 정렬할 큐
for i in range(n):
    flower[i]=list(map(int,input().split()))
    q.append((-flower[i][2],-flower[i][3],flower[i][0],flower[i][1],i))
q.sort()
while q:#큐가 빌 때까지
    m=q.pop(0)[4] #최대 날짜의 꽃 인덱스 꺼냄
    if flower[m][2]<max[0] or (flower[m][2]==max[0] and flower[m][3]<max[1]):
        break #원하는 기간을 채울 수 없을 때
    else: #기간을 cover할 수 있을 때
        if(flower[m][0]<min[0] or flower[m][0]==min[0] and flower[m][1]<=min[1]): #최소 날짜보다 작으면 끝
            select.append(m) #선택. 시작 달 기준 정렬
            break
        max[0],max[1]=flower[m][0],flower[m][1] #꽃의 개화일을 max로 둔다
        select.append(m) #선택. 시작 달 기준 정렬
select.sort()
def cal_date(month,day):
    print(date[month]+day)
    return date[month]+day
print(select)
'''count=0
i=-1
print(select)
while select: #선택한 큐가 빌 때까지 겹치는 기간의 꽃 삭제
    if len(select)<3 and i==-1: #3개 미만의 꽃일 때는 겹치는 거 없음
        count+=len(select)
        print("!first")
        break
    if(i==-1 and len(select)>=3):#아직 안 꺼냈고 3개 이상의 꽃일 때
        i=heapq.heappop(select) #처음 꽃의 인덱스
        j=heapq.heappop(select) #중간 꽃의 인덱스
        k=heapq.heappop(select) #마지막 꽃의 인덱스
        print("!second")
        count+=3
    elif(i>-1 and len(select)>=1): #꺼냈고 더 꺼낼 게 남았으면
        i=j #처음 꽃의 인덱스
        j=k
        k=heapq.heappop(select) #다음 꽃의 인덱스
        print("!third")
        count+=1
    if(cal_date(flower[k][0],flower[k][1])-cal_date(flower[i][2],flower[i][3])<=0):
        print("!fourth")
        count-=1 #중간 게 겹칠 때
        
print(count)
'''
'''
date={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
min=60 #공주가 원하는 시작일 59+1(3월 1일)
max=334 #공주가 원하는 마감임 304(11월 30일)
'''



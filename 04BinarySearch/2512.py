#백준 2512-예산
#특정 정수 상한액->나눠줄 수 있는 예산의 합이 최대가 되게
from sys import stdin
input=stdin.readline
n=int(input()) #지역 수
req=list(map(int,input().split()))
m=int(input()) #실제 예산
start=0  #중요!!!!!!!!!!!mid가 min(req)보다 작을 수 있다
end=max(req)
result=0

def BS(start,end):
    global result,m
    while(start<=end):
        total=0 #실제 분배한 예산의 총 합
        temp=0 #분배한 예산 중 최대
        mid=(start+end)//2 #상한액
        for x in req:
            if x>mid: #요청이 상한액보다 크면 상한액만큼 분배
                total+=mid #전체 분배한 예산 누적
                temp=max(temp,mid)
            else: #요청이 더 작으면 요청만큼 분배
                total+=x
                temp=max(temp,x)
        if total<=m: #예산을 만족하는 경우 상한액 늘리기
            start=mid+1
            result=max(result,temp)
        else: #예산을 초과하는 경우 상한액 줄이기
            end=mid-1
BS(start,end)
print(result)
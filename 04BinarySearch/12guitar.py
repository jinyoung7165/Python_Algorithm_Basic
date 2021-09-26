#백준 2343 - 기타레슨
#n개의 강의 '순서대로' 녹화. i번과 j번 강의를 같이 녹화하려면 i와 j사이의 모든 강의를 녹화해야 함
#블루레이 개수를 가급적 줄이려고 함. m개의 블루레이에 모든 강의를 담기로
#블루레이의 크기(녹화 길이)를 최소화하려고 함
#각 강의 길이가 주어질 때, 가능한 블루레이의 길이 중 최소
#강의 수n 블루레이 개수m와 각 강의 길이가 주어짐
#각 강의를 블루레이에 집어넣었을 때, 블루레이의 크기는 강의 길이의 합 중 최댓값
#mid는 블루레이의 크기. 다 저장 못하면 start증가시킴. 저장 가능하면 end를 감소시켜 최소 mid 찾음
from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
course=list(map(int,(input().split())))#각 강의 길이
end=sum(course)
start=sum(course)//m #박스 수로 sum을 나누
result=sum(course) #중요!!!!!!!!!!!min을 구해야하기 때문에 나올 수 있는 가장 최댓값

while (start<=end):
    mid=(start+end)//2
    temp,count=0,0 #한 박스에 저장된 영상길이, 몇 개의 박스를 꽉 채웠는지
    if (max(course)>mid): #애초에 저장 불가
        start=mid+1
        continue
    for i in range(n):
        if (temp+course[i]<=mid):#이번 걸 저장해도 블루레이 용량이 남을 때
            temp+=course[i] #저장
        else: 
            count+=1 #이전까지 하나의 블루레이 다 채움
            temp=course[i] #다음 블루레이에 저장
    if(count<=m-1):#정해진 블루레이 개수-1만큼 다 채우고 (마지막 박스까지 채웠을 수도 있다)
        end=mid-1 #mid 감소시킬 것임
        result=min(mid,result)
    else:#블루레이 개수 초과했을 때
        start=mid+1 #블루레이의 크기 증가시킬 거임

print(result)

#국어점수가 감소하는 순
#영어점수가 증가하는 순
#수학점수가 감소하는 순
#이름이 사전순으로 증가하는 순(아스키코드에서 대문자는 소문자보다 작으므로 사전순으로 정렬)
from collections import deque
n=int(input())#학생 수
arr=[]
for i in range(n):
    data=input().split()
    arr.append((data[0],int(data[1]),int(data[2]),int(data[3])))
arr.sort(key=lambda score:score[1])
que=deque()
for i in range(n):
    if(arr[i][1]==arr[i+1][1]):
        que.append(i,i+1)
        
arr.sort(key=lambda score:score[2])
arr.sort(key=lambda score:score[3])
arr.sort(key=lambda score:score[0])
for i in range(n):
    print(arr[i][0])

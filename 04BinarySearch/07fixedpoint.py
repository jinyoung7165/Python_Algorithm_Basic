#고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
#하나의 수열이 N개의 서로 다른 원소를 포함. 고정점 출력
#고정점이 나오고 나서, 그 다음 원소가 고정점이 아니라면 그 후 고정점은 없다
from bisect import bisect_right,bisect_left
arr=list(map(int,input().split()))
mid=(max(arr)+min(arr))//2
right_idx=bisect_right(arr,mid)
left_idx=bisect_left(arr,mid)
flag=False #고정점 발견하면 true
while left_idx<right_idx:
    if(arr[left_idx]==left_idx):
        print(left_idx)  #고정점 출력
        flag=True
    if(flag==True and arr[left_idx]!=left_idx):break #더 이상 고정점 없음
    left_idx+=1

if(flag==False or (left_idx==right_idx and flag==True)):
    while right_idx<len(arr):
        if(arr[right_idx]==right_idx):
            print(right_idx)
            flag=True
        if(flag==True and arr[right_idx]!=right_idx):break
        right_idx+=1
if(flag==False):print(-1)


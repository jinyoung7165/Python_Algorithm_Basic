#고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
#하나의 수열이 N개의 서로 다른 원소를 포함. 고정점 출력
#고정점이 나오고 나서, 그 다음 원소가 고정점이 아니라면 그 후 고정점은 없다
def binary(arr,start,end):
    if start>end: return None
    mid=(start+end)//2
    if arr[mid]==mid:
        return mid
    elif arr[mid]>mid:
        binary(arr,start,end-1)
    else: binary(arr,start+1,end)
n=int(input())
arr=list(map(int,input().split()))
index=binary(arr,0,n-1)
if index==None:print(-1)
else: print(index)

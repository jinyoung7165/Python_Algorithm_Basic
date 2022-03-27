def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2 #중간점
    if arr[mid]==target:#찾을 값이 중간점 위치에 있을 때
        return mid #찾은 경우 중간점 인덱스 리턴
    elif arr[mid]>target:#중간점 값보다 찾을 값이 작을 때 왼쪽 확인
        return binary_search(arr,target,start,mid-1)
    else:#찾을 값이 더 크면 중간점 위치의 오른쪽 확인
        return binary_search(arr,target,mid+1,end)
n,target=list(map(int,input().split()))#원소 개수와 찾을 값
arr=list(map(int,input().split()))#전체 원소 입력
result=binary_search(arr,target,0,n-1)
if result==None:
    print("원소가 존재하지 않음")
else: print(result+1)#몇번째 원소인지
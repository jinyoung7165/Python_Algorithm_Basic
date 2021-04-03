def binary(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target: #찾은 경우 중간점 인덱스 반환
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input()) #손님이 확인요청한 부품 개수
x=list(map(int,input().split())) #손님이 확인 요청한 부품번호 리스트
for i in x: #해당 부품이 존재하는지 확인
    result=binary(arr,i,0,n-1)
    if result!=None:
        print('yes',end='')
    else: print('no',end='')
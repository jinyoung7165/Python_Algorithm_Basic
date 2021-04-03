#n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음
#이 수열에서 x가 등장하는 횟수
#{1,1,2,2,2,2,3}, x=2라면 값이 2인 원소가 4개이므로 4 출력
#특정값이 등장하는 첫번째 위치와 마지막 위치를 찾아 위치 차이를 계산
#O(logN)으로 동작
from bisect import bisect_left,bisect_right
#값이 [left,right] 범위인 데이터의 개수를 반환
def count_by_range(arr,left,right):
    right_idx=bisect_right(arr,right)
    left_idx=bisect_left(arr,left)
    return right_idx-left_idx
n,x=map(int,input().split())#데이터개수,찾을 값
arr=list(map(int,input().split()))#전체 데이터 입력
count=count_by_range(arr,x,x)#값이 [x,x] 범위에 있는 데이터의 개수 계산
if count==0:#값이 x인 원소가 존재하지 않는다면
    print(-1)
else:#값이x인 원소가 존재한다면
    print(count)
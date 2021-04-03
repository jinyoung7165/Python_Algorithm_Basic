from bisect import bisect_right,bisect_left
#값이 [left,right] 범위인 데이터의 개수를 반환
def count_by_range(a,left,right):
    right_idx=bisect_right(a,right)
    left_idx=bisect_right(a,left)
    return right_idx-left_idx
a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))#값이 4인 데이터 개수 출력
print(count_by_range(a,-1,3))#값이 [-1,3] 범위에 있는 데이터의 개수 출력
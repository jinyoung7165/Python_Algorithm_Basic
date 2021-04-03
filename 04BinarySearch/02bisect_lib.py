from bisect import bisect_left,bisect_right
a=[1,2,4,4,8]
x=4
print(bisect_left(a,x))#정렬 유지하며 배열a에 x를 삽입할 가장 왼쪽 인덱스2
print(bisect_right(a,x))#4
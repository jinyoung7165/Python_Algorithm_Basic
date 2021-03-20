'''
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장
n x m 카드 
행 선택, 가장 낮은 카드
'''
n,m=map(int,input().split()) #행,열
min=[0]*m
for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort()
    min[i]=arr[0]
min.sort(reverse=True)
print(min[0])

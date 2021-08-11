#10815 숫자카드
#숫자 카드 n개를 가지고 있고, M개의 정수들이 주어졌을 때 해당 카드를 가지고 있는지 1,0출력
from sys import stdin
from bisect import bisect_left,bisect_right
input=stdin.readline

def count_by_range(arr,left,right):
    right_idx=bisect_right(arr,right)
    left_idx=bisect_left(arr,left)
    if(right_idx-left_idx>0):return 1
    else:return 0

n=input()
card,num=[],[]
card=list(map(int,input().split()))
card.sort() #필수!
m=int(input())
num=list(map(int,input().split()))
for i in range(m):
    number=num[i] #찾아야하는 숫자
    print(count_by_range(card,number,number),end=' ')

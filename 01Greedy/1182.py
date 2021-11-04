#백준 1182- 부분수열의 합
#N개의 정수로 이뤄진 수열의 부분수열 중
#모든 원소의 합이 S가 되는 경우의 수
#포함/포함x
from sys import stdin
from itertools import combinations
input=stdin.readline
n,s=map(int,input().split())
sequence=list(map(int,input().split()))

count=0
for i in range(1,n+1): #길이 1~n인 부분수열
    sub=combinations(sequence,i)
    for j in sub: #부분수열 j
        if(sum(j)==s):
            count+=1
print(count)
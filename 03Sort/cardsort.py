#정렬된 두 묶음의 숫자 카드
#10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요
from queue import PriorityQueue
from sys import stdin
input=stdin.readline
n = int(input())#n개 줄에 걸쳐 숫자 카드 묶음의 크기가 주어짐
#최소 비교횟수를 출력
que=PriorityQueue()
real=0
for i in range(n):
    que.put(int(input()))
for _ in range(n-1):
    sum=0
    sum=que.get()+que.get()
    real+=sum
    que.put(sum)
print(real)
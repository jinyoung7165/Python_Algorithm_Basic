#국어점수가 감소하는 순
#영어점수가 증가하는 순
#수학점수가 감소하는 순
#이름이 사전순으로 증가하는 순(아스키코드에서 대문자는 소문자보다 작으므로 사전순으로 정렬)
from sys import stdin
n = int(stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(stdin.readline().split()))
new=sorted(arr,key=lambda score:(-int(score[1]),int(score[2]),-int(score[3]),score[0]))
for student in new:
    print(student[0])

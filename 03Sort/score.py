#성적이 낮은 순으로 학생 이름 출력
n=int(input())#학생 수
arr=[]
for i in range(n):
    data=input().split() #이름 성적
    arr.append((data[0],int(data[1])))
arr.sort(key=lambda student:student[1])
for i in arr:
    print(i[0],end='')


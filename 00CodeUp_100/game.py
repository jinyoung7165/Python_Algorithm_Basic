a=input()
n=int(a)
b=input().split() #부른번호
arr=[]
for i in range(24):
    arr.append(0)
for i in range(n):
    arr[int(b[i])]+=1
for i in range(1, 24) : print(arr[i], end=' ')



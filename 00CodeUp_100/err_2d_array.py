a=int(input())
arr=[]
arr=[]

for i in range(19):
    arr.append([])
    for j in range(19):
        arr[i].append(0)
for j in range(a):
    b,c=input().split()
    b=int(b)
    c=int(c)
    arr[b-1][c-1]=1

for i in range(19):
    for j in range(19):
        print('%d'%arr[i][j],end=' ')
   
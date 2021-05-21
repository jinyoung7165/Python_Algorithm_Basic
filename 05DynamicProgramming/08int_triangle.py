n=int(input())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:  #첫번째 열일 때 왼쪽 위는 없다
            up_left=0
        else:
            up_left=triangle[i-1][j-1] #왼쪽 위에서 올 때
        if j==i:#행의 마지막 열일 때 오른쪽 위는 없다
            up_right=0
        else: 
            up_right=triangle[i-1][j] #오른쪽 위에서 올 때
        triangle[i][j]+=max(up_right,up_left)

print(max(triangle[n-1])) #마지막 열의 원소로 내려왔을 때 가장 큰 합

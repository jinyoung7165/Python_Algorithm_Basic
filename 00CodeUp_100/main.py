a=input()
n=len(list(a))

for i in list(a):
    print("[%s"%(i),end='')
    for j in range(0,n-1):
        print("0",end='')
    n=n-1
    print("]")


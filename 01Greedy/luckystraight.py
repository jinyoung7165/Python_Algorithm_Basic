n=input()
half=len(n)//2  #//로 나눠야 int주의!!!!
a=0
b=0
for i in n[:half]:
    a+=int(i)
for i in n[half:]:
    b+=int(i)

if a==b:
    print("LUCKY")
else:
    print("READY")


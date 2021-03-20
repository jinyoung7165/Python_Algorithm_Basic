'''
수평으로 두 칸 이동 후 수직으로 한 칸
수직으로 두 칸 이동 후 수평으로 한 칸
'''

count=0
state=input() #현재 위치
col=['a','b','c','d','e','f','g','h']
row=['1','2','3','4','5','6','7','8']
x=col.index((state[0]))+1
y=row.index((state[1]))+1

# 동,서,남,북
dx=[0,0,-1,1]
dy=[-1,1,0,1]

for i in range(4):
    if(i==0 or i==1): #수직이동*2
        if(0<x+2*dx[i]<8):
            if(0<y+dy[i]<8):
                count+=1
        else: break

    else: #수평이동*2
        if(0<y+2*dy[i]<8):
            if(0<x+dx[i]<8):
                count+=1
        else: break

print(count)    
'''
nx=x+2*dx
ny=y+dy
nx=x+dx
ny=y+2*dy
'''
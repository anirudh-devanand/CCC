import random
inp=input().split()
n=int(inp[0])
m=int(inp[1])
k=int(inp[2])
count=0
c=0
piece=''
while True:
    x=0
    for i in range(n):
        val=str(random.randint(1,m))
        if val not in piece:
            c+=x
        else:
            count+=c
            c==0
            x==-1
        x+=1
    if count==k:
        break
    piece=''


print(piece)


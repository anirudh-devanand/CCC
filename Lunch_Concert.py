import math
k=int(input())
fren=[[] for i in range(k)]
mn,mx=math.inf,0
for i in range(k):
    inp=input().split()
    mn=min(mn,int(inp[0]))
    mx=max(mx,int(inp[0]))
    fren[i].append(float(inp[0]))
    fren[i].append(float(inp[1]))
    fren[i].append(float(inp[2]))

best=math.inf
flag=0
for d in range(mn,mx+1):
    time=0
    for n in fren:
        if n[2]< abs(n[0]-d):
            time+=(abs(n[0]-d)-n[2])*n[1]
            if time>=best:
                break
    if time>=best:
            break
    best=min(best,time)

print (int(best))

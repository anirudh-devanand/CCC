g=int(input())
p=int(input())
occupied=[]
gi=[int(input()) for i in range(p)]
best=0
count=0
def solve(x):
    global count
    global best
    if not count==p:
        for i in range(gi[x]):
            if i not in occupied:
                occupied.append(i)
                count+=1
                solve(x+1)
                occupied.remove(i)
                count-=1
        best=max(best,count)
    else:
        return p
    return best

print(solve(0))

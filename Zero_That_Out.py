tot=[]
k=int(input())
for i in range(k):
    temp=int(input())
    if not temp==0:
        tot.append(temp)
    else:
        tot.pop()

print(sum(tot))
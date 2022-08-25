inp=[]
for x in range(int(input())):
    temp=input().split()
    inp.append([float(temp[0]),temp[1]])
inp.sort()

bst_spd=0
for x in range(1,len(inp)):
    bst_spd=max(bst_spd,abs(float(inp[x][1])-float(inp[x-1][1]))/(inp[x][0]-inp[x-1][0]))

print(bst_spd)
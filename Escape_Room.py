import sys
sys.setrecursionlimit(10*8)

m,n=int(input()),int(input())
arr= [input().split() for i in range(m)]
can='no'
visited=[]


def jump(x,y):
    global can
    if can=='yes':
        return
    if x==len(arr)-1 and y==len(arr[0])-1:
        can='yes'
        return
    if [x+1,y+1, arr[x][y]] not in visited:
        visited.append([x+1,y+1, arr[x][y]])
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i+1)*(j+1)==int(arr[x][y]):
                    jump(i,j)
                if can=='yes':
                    break
        visited.remove([x+1,y+1, arr[x][y]])
    else:
        return

    return can

print(jump(0,0))
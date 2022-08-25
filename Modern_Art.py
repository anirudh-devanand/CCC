m=int(input())
n=int(input())
k=int(input())
choice=[]
row=0
for i in range(k):
    inp=input()
    if inp not in choice:
        choice.append(inp)
        if 'R' in inp:
            row+=1
    else:
        choice.remove(inp)
        if 'R' in inp:
            row-=1

col=len(choice)-row

print((row*n)+(col*m)-2*(col*row))
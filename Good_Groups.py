x=int(input())
constraints=[(input()+' together').split() for i in range(x)]
y=int(input())
for i in range(y):
    constraints.append((input()+' seperate').split())
g=int(input())
groups=[input().split() for i in range(g)]
count=0

for elem in constraints:
    if 'together' in elem:
        for group in groups:
            if (elem[0] in group and elem[1] not in group) or (elem[1] in group and elem[0] not in group):
                count+=1
                break
    if 'seperate' in elem:
        for group in groups:
            if elem[0] in group and elem[1] in group:
                count+=1

print(count)
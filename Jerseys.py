j=int(input())
a=int(input())
count=0

jer=[]
for i in range(j):
    jer.append(input()+' '+str(i+1))

ath=[input() for i in range(a)]

for choice in ath:
    if 'S' in choice:
        if choice in jer:
            jer.pop(jer.index(choice))
            count+=1
        elif ('M '+choice.spilt[-1]) in jer:
            jer.pop('M '+choice.spilt[-1])
            count+=1
        elif ('L '+choice.spilt[-1]) in jer:
            jer.pop('L '+choice.spilt[-1])
            count+=1

    elif 'M' in choice:
        if choice in jer:
            jer.pop(jer.index(choice))
            count+=1
        elif ('L '+choice.spilt[-1]) in jer:
            jer.pop('L '+choice.spilt[-1])
            count+=1

    elif 'L' in choice:
        if choice in jer:
            jer.pop(jer.index(choice))
            count+=1

print(count)

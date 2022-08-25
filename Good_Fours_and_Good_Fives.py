from math import floor
n=int(input())
four=0
while n>0:
    n-=4
    four+=1
if not n==0:
    four-=5+n

if four<0:
    print(0)
else:
    print(1+int(floor(four/5)))

num=int(input())
heights=list(map(int,input().split()))
widths=list(map(int,input().split()))
area=0
for i in range(num):
    area+=(widths[i]*(min(heights[i],heights[1+i])))+((max(heights[i],heights[i+1])-min(heights[i],heights[i+1]))*0.5*widths[i])
print(area)
def maxvalue(a,b):
    maximalvalue=0
    for i in range (a,b+1):
        for j in range (i,b+1):
            curvalue=i^j
            maximalvalue=max(maximalvalue,curvalue)
    print(maximalvalue)
a=int(input())
b=int(input())
maxvalue(a,b)

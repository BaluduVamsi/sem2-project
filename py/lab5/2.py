def pieces(x):
    if x%2==0:
        c=x/2*x/2
    else:
        c=(x-1)/2*(x+1)/2
    print(c)
t=int(input())
for i in range(t):
    a=int(input())
    pieces(a)


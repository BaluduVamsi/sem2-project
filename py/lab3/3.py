def heightofutop(n):
    height=1
    i=1
    while i<=n:
        if i%2!=0:
            height*=2
            i+=1
        else:
            height+=1
            i+=1
    print(height)
t=int(input("no of test cases"))
for i in range(t):
    c=int(input("enter number of cycles"))
    heightofutop(c)

    
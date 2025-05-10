def myst(t):
    n=len(t)
    c=0
    for i in range(n//2):
        a=ord(t[i])
        b=ord(t[n-i-1])
        if a!=b:
           c=c+abs(a-b)
    print(c)
a=int(input("enter no of testcases"))
for i in range(a):
    b=input("enter the testcase ")
    myst(b)          
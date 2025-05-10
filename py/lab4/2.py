def isperfect(x):
    s=int(x**0.5)
    return s**2==x
def noofsquares(k,l):
     a=0
     for i in range(k,l+1):
          if isperfect(i):
               a+=1
     print(a)
a=int(input("enter no of test cases"))
for i in range(a):
     a,b=map(int,input().split())
     noofsquares(a,b)
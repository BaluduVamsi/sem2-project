def isperfect(x):
    s=int(x**0.5)
    return s**2==x
def isfibo (x):
    if isperfect(5*x**2+4) or isperfect(5*x**2-4):
        print("is fibo")
    else:
        print("is not fibo")
n=int(input("enter no of test cases"))
for i in range(n):
    t=int(input("Enter number"))
    isfibo(t)
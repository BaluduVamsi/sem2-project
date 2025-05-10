def digitalroot (n):
    c=n
    sum=0
    while n>10:
        sum=sum+n%10
        n=int(n/10)
        if n<10:
            print(f"digital root of {c}is{n}")
n=int(input("enter the number"))
digitalroot(n)
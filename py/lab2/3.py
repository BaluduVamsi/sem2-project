t = int(input("noofnumbers"))  
for _ in range(t):  
    n = input("enter number")
    c=0
    for i in range(len(n)):
        d=n[i]
        if int(n)%int(d)==0:
           c=c+1
    print("no of digits",c)
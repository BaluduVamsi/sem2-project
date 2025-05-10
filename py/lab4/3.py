def pangram(t):
    ispangram=1
    i=97
    while i!=123:
        for j in t:
            a=ord(j)
            if a==i:
                i=i+1
                break
        else:
            ispangram=0
            break
                
    if ispangram :
        print("is pangram")
    else:
        print("isnotpangram")
a=input("enter the sentence")
pangram(a)

def swap(b,c,t):

    newtext=t.replace(b,'3').replace(c,b).replace('3',c)
    print(newtext)

def lexi(a):
    t=len(a)
    for i in range(t-2,-1,-1):
       if ord(a[i])<ord(a[i+1]):
           smallestnum=1000
           for j in range(i+1,t):
               k=ord(a[j])
               smallestnum=min(smallestnum,k)
           swap(a[i],chr(smallestnum),a)
           break
    else:
        print("no answer")
t=int(input())
for i in range(t):
    a=input()
    lexi(a)
a=input("enter the number:")
def decode(a,i=0,result=None,k=""):
   if result is None:
      result=[]
   if i==len(a):
      result.append(k)
      return
   num1=int(a[i])
   if 1<=num1<=9:
      decode(a,i+1,result,k+chr(num1+64))
   if i+1<len(a):
      num2=int(a[i:i+2])
      if 10<=num2<=26:
         decode(a,i+2,result,k+chr(num2+64))
   return result
print(decode(a))
def span(prices):
    span = [0] * len(prices)
    for i in range(len(prices)) :
         span[i]=1
         j=i-1
         while j>=0 and prices[j]<=prices[i] :
                     span[i]+=1
                     j-=1
    print(span)              
k=input("enter the price for n days separated by space" )   
k_=list(map(int,k.split()))
span(k_)           
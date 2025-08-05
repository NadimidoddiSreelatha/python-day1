def fun(n):
    if n==0:
        return 0
    return 1+fun(n//10)
c=fun(1729)
print(c)









def wish(n):
    if n==1:
       print(n)
       return
   print(n)
   wish(n-1)
   print(n)
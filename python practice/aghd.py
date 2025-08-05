n=int(input())
reverse=0
while n>0:
    n=n%10
    reverse=reverse*10+n
    n//10
print("reversed number",reverse)






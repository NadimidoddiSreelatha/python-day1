s=input()
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c=c+1
print(c)







n=int(input())
m=int(input())
l=[]
for i in range(n,m):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
            break
    else:
        l.append(i)
print(l)
            

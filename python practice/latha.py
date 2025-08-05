n=153
sum=0
s=str(n)
temp=len(s)
for i in s:
    sum+=int(i)**temp
print(sum)






n=153
sum=0
s=str(n)
temp=len(s)
for i in s:
    sum+=int(i)**temp
if sum==n:
    print("Armstrong")
else:
    print("Not Armstrong")






m=0
n=1
print(m)
print(n)
for i in range(3,10):
    print(m+n)
    t=m+n
    m=n
    n=t





l=[1,1,2,2,3,4,4]
s=set(l)
print(s)





s={1,2,3,4,5,6,7}
p={7,8,9,10,11}
t=s.pop()
print(t)
s.add(8)
print(s)
a=s.union(p)
print(a)
b=s.difference(p)
print(b)
c=s.symmetric_difference(p)
print(c)
d=s.intersection(p)
print(d)



l=[10,20,15,19,18,13,12,22]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
sum=0
for i in range(0,8):
    sum=sum+l[i]
print("sum of",n,"is",sum)









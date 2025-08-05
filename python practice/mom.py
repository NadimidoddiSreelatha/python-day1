l=[100,10,21,40,39,101,51]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
l=[100,10,21,40,39,101,51]
even=[]
odd=[]
for i in range(0,len(l),1):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
print(even)
print(odd)
l=[1,10,57,4,56,43,79]
print("Index->Element")
for i in range(0,len(l),1):
    print(i,"->",l[i])
l=[100,10,21,40,39,101,51]
even=[]
odd=[]
for i in range(0,len(l),1):
    if i%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
print(even)
print(odd)
a=1
b=bool(a)
print(type(b))
j=chr(a)
print(type(j))
s={1,2,3}
print(type(s))
b=list(s)
print(type(b))
print(b)
print(s)
n=10
print(type(n))
c=float(n)
print(type(c))
print(c)
a=1
print(type(a))
d=bool(a)
print(type(d))
print(d)
print(a)
s="sreelatha"
print(type(s))
print(s)
d=list(s)
print(d)
print(type(d))
s=[1,2,4,6,8]
print(s)
e=set(s)
print(e)
print(type(e))
k=9
k=complex(a)
print(k)
print(type(k))
for i in range(0,10):
    print(i)
    if i==5 or i==8:
        continue
    print("hai")
for i in range(0,10):
    if i==5: 
        break
    print(i)
a=float(input())
print(type(a))
print("My name is",a)
a=float(input())
b=float(input())
print(a+b)
l=[]
for i in range(5):
    a=int(input())
    l.append(a)
print(l)
n="171"
b=n[::-1]
if(a==b):
    print("palindrome")
else:
    print("not palindrome")


   







































n=7
c=0
for i in range(2,7):
    if n%i==0:
        c+=1
if c==0:
        print("Prime number")
else:
        print("Not prime number")











s=input()
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c=c+1
print(c)
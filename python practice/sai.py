n=135
s=0
s=str(n)
temp=len(s)
for i in s:
    s=int(i)**temp
if n==int(s):
    print("armstrong")
else:
    print("Not armstrong")
n=153
s=0
s=str(n)
temp=len(s)
for i in s:
    s=int(i)**temp
if n==int(s):
    print(s)
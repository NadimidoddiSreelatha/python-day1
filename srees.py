str="All silver tea cups."
str=input().lower()
count=0
for i in str:
    if i in "aeiou":
        count=count+1
print(count)
    

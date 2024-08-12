n=input()
str1=""
for i in range(1,len(n)):
    if n[i]==n[i].upper():
        str1=str1+" "+n[i].upper()
    else:
        str1=str1+n[i]
print(n[0]+str1)